from collections.abc import Callable
from typing import Self

from gallery_dl.exception import NoExtractorError
from gallery_dl.extractor import find as find_extractor
from gallery_dl.extractor.common import Extractor
from gallery_dl.util import SPECIAL_EXTRACTORS, build_extractor_filter

from .downloader import Downloader
from .extra_types import KWDict
from .file import File
from .message import DirectoryMessage, QueueMessage, URLMessage, parse_message


class DownloadJob:
    extractor: Extractor
    visited: set[str]
    _metadata: KWDict
    finished: bool = False
    _files: tuple[File, ...]
    _children: list[Self]

    def __init__(self, extractor: Extractor | str, parent: Self | None = None) -> None:
        if isinstance(extractor, str):
            found_extractor = find_extractor(extractor)
            if found_extractor is None:
                raise NoExtractorError(extractor)
            else:
                self.extractor = found_extractor
        else:
            self.extractor = extractor

        self._files = ()
        self._children = []
        self._metadata = {}

        self.parent = parent
        self.visited = parent.visited if parent else set()

        self.filter_extractor = self._build_extractor_filter()

    @property
    def files(self) -> tuple[File, ...]:
        if not self.finished:
            raise ValueError("Can't access files before running job with `.run()`")
        files = self._files
        for child in self._children:
            files += child.files
        return files

    @property
    def metadata(self) -> KWDict:
        metadata = self._metadata | {
            "category": self.extractor.category,
            "subcategory": self.extractor.subcategory,
            "basecategory": self.extractor.basecategory,
        }
        for child in self._children:
            metadata = metadata | child.metadata
        return metadata

    def _build_extractor_filter(self) -> Callable[[Extractor], bool]:
        clist = self.extractor.config("whitelist")
        if clist is not None:
            negate = False
            special = None
        else:
            clist = self.extractor.config("blacklist")
            negate = True
            special = SPECIAL_EXTRACTORS
            if clist is None:
                clist = (self.extractor.category,)

        return build_extractor_filter(clist, negate, special)

    def run(self) -> None:
        self.extractor.initialize()

        for message in self.extractor:
            message = parse_message(message)

            if isinstance(message, DirectoryMessage):
                self._metadata = self._metadata | message.metadata

            if isinstance(message, URLMessage):
                if message.url in self.visited:
                    continue
                else:
                    self.visited.add(message.url)

                downloader = Downloader(self.extractor)
                self._files += (downloader.download(message.url, message.metadata),)

            elif isinstance(message, QueueMessage):
                if message.url in self.visited:
                    continue
                else:
                    self.visited.add(message.url)

                if extractor_class := message.metadata.get("_extractor"):
                    assert isinstance(extractor_class, type) and issubclass(
                        extractor_class, Extractor
                    )
                    child_extractor = extractor_class.from_url(message.url)
                else:
                    child_extractor = find_extractor(message.url)
                    if child_extractor and not self.filter_extractor(child_extractor):
                        # Doesn't pass the configured filter
                        continue
                if child_extractor is None:
                    raise Exception("No extractor :(")  # TODO

                child_job = self.__class__(child_extractor, self)
                child_job.run()
                self._children.append(child_job)

            else:
                # We don't need to worry about version messages
                pass

        self.finished = True
