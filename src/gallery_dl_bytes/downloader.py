from collections.abc import Callable
from dataclasses import InitVar, dataclass, field
from io import BufferedIOBase, BytesIO
from pathlib import PurePath
from ssl import SSLError
from textwrap import dedent
from time import monotonic, sleep
from typing import Any, cast

import gallery_dl.config
from gallery_dl.extractor.common import Extractor
from gallery_dl.formatter import StringFormatter
from gallery_dl.formatter import parse as parse_filename
from gallery_dl.text import parse_bytes
from requests import Session
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import RequestException, Timeout

from .extra_types import KWDict
from .file import File


@dataclass
class DownloaderSettings:
    init_filesize_min: InitVar[str | int | None]
    filesize_min: int | None = field(init=False)
    init_filesize_max: InitVar[str | int | None]
    filesize_max: int | None = field(init=False)
    init_chunk_size: InitVar[str | int | None]
    chunk_size: int | None = field(init=False)
    init_download_rate_max: InitVar[str | int | None]
    download_rate_max: int | None = field(init=False)

    retries_max: int | float
    retry_codes: list[int]
    timeout: float

    headers: dict[str, str]
    verify_tls: bool | str
    mtime_from_http: bool
    adjust_extensions: bool

    def __post_init__(
        self,
        init_filesize_min: str | int | None,
        init_filesize_max: str | int | None,
        init_chunk_size: str | int | None,
        init_download_rate_max: str | int | None,
    ) -> None:
        if self.retries_max < 0:
            self.retries_max = float("inf")

        if isinstance(init_filesize_min, str):
            if not (filesize_min := parse_bytes(init_filesize_min)):
                raise ValueError(f"Invalid minimum file size {init_filesize_min}")
            self.filesize_min = filesize_min
        else:
            self.filesize_min = init_filesize_min

        if isinstance(init_filesize_max, str):
            if not (filesize_max := parse_bytes(init_filesize_max)):
                raise ValueError(f"Invalid maximum file size {init_filesize_max}")
            self.filesize_max = filesize_max
        else:
            self.filesize_max = init_filesize_max

        if isinstance(init_chunk_size, str):
            if not (chunk_size := parse_bytes(init_chunk_size)):
                raise ValueError(f"Invalid chunk size {init_chunk_size}")
            self.chunk_size = chunk_size
        else:
            self.chunk_size = init_chunk_size

        if isinstance(init_download_rate_max, str):
            if not (download_rate_max := parse_bytes(init_download_rate_max)):
                raise ValueError(f"Invalid download rate maximum limit {self.download_rate_max}")
            self.download_rate_max = download_rate_max
        else:
            self.download_rate_max = init_download_rate_max

        if self.download_rate_max and self.chunk_size and self.download_rate_max < self.chunk_size:
            raise ValueError(
                dedent(f"""
                Chunk size ({self.chunk_size}) must be less than or equal to download rate maximum
                ({self.download_rate_max})
""")
            )


class Downloader:
    session: Session
    _formatter: Callable[[KWDict], str]

    def __init__(self, extractor: Extractor) -> None:
        self.session = extractor.session
        self._formatter = cast(StringFormatter, parse_filename(extractor.filename_fmt)).format_map
        self.downloading = False

        if hasattr(extractor, "_proxies"):
            pass  # TODO

        self.settings = DownloaderSettings(
            init_filesize_min=self._interpolate_config("filesize-min"),
            init_filesize_max=self._interpolate_config("filesize-max"),
            init_chunk_size=self._interpolate_config("chunk-size", 32768),
            init_download_rate_max=self._interpolate_config("rate"),
            retries_max=self._interpolate_config("retries", extractor._retries),
            retry_codes=self._interpolate_config("retry-codes", extractor._retry_codes),
            timeout=self._interpolate_config("timeout", extractor._timeout),
            headers=self._interpolate_config("headers"),
            verify_tls=self._interpolate_config("verify", extractor._verify),
            mtime_from_http=self._interpolate_config("mtime", True),
            adjust_extensions=self._interpolate_config("adjust-extensions", True),
        )

    def _interpolate_config(self, key: str, default: Any = None) -> Any:
        return gallery_dl.config.interpolate(("downloader", "http"), key, default)

    def build_filename(self, metadata: KWDict) -> PurePath:
        return PurePath(self._formatter(metadata))

    def download(self, url: str, metadata: KWDict) -> File:
        tries = 0

        while True:
            if tries > self.settings.retries_max:
                raise Exception("Couldn't download")  # TODO: proper exception class
            sleep(tries)
            tries += 1

            headers = {"Accept": "*/*"}
            if self.settings.headers:
                headers.update(self.settings.headers)

            try:
                response = self.session.request(
                    method="GET",
                    url=url,
                    stream=True,
                    headers=headers,
                    timeout=self.settings.timeout,
                    verify=self.settings.verify_tls,
                )
            except (RequestsConnectionError, Timeout):
                #  Ignore, return to top of loop and give it another try
                continue

            if response.status_code in (206, 416):
                raise NotImplementedError("Partial downloads not implemented yet")  # TODO
            if response.status_code != 200:
                raise Exception(f"Couldn't download: {response.status_code}: {response.reason}")

            size_header = response.headers.get("Content-Length")
            size = None
            if size_header is not None:
                try:
                    size = int(size_header)
                    if self.settings.filesize_min and size < self.settings.filesize_min:
                        raise Exception(f"File too small (size {size})")  # TODO
                    if self.settings.filesize_max and size > self.settings.filesize_max:
                        raise Exception(f"File too large (size {size})")
                except ValueError:
                    pass

            mime_type = response.headers.get("Content-Type")
            if mime_type:
                mime_type = mime_type.partition(";")[0]
                mime_type = mime_type if "/" in mime_type else f"image/{mime_type}"

            # TODO: determine filename and extension

            self.downloading = True
            content = response.iter_content(self.settings.chunk_size)
            with BytesIO() as buffer:
                try:
                    self._receive(buffer, content)
                except (RequestException, SSLError):
                    continue
                data = buffer.getvalue()

            # If we got here, we're all done!
            break

        self.downloading = False
        return File(
            name=self.build_filename(metadata),
            headers=response.headers,
            data=data,
            metadata=metadata,
        )

    def _receive(self, buffer: BufferedIOBase, content: Any) -> None:
        if self.settings.download_rate_max:
            bytes_downloaded = 0
            time_start = monotonic()

            for data in content:
                time_elapsed = monotonic() - time_start
                bytes_downloaded += len(data)

                _ = buffer.write(data)

                time_expected = bytes_downloaded / self.settings.download_rate_max
                if time_expected > time_elapsed:
                    sleep(time_expected - time_elapsed)

        else:
            for data in content:
                _ = buffer.write(data)
