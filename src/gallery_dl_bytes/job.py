from collections.abc import Callable
from typing import Self

from gallery_dl.extractor import find as find_extractor
from gallery_dl.extractor.common import Extractor
from gallery_dl.util import SPECIAL_EXTRACTORS, build_extractor_filter

from .downloader import Downloader
from .file import File
from .message import QueueMessage, URLMessage, parse_message


def download(url: str) -> list[File]:
    return DownloadJob(url).run()


class DownloadJob:
    extractor: Extractor
    visited: set[str]

    def __init__(self, extractor: Extractor | str, parent: Self | None = None) -> None:
        if isinstance(extractor, str):
            found_extractor = find_extractor(extractor)
            if found_extractor is None:
                raise Exception("No extractor found")
            else:
                self.extractor = found_extractor
        else:
            self.extractor = extractor

        self.parent = parent
        self.visited = parent.visited if parent else set()

        self.filter_extractor = self._build_extractor_filter()

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

    def run(self) -> list[File]:
        self.extractor.initialize()
        files: list[File] = []

        for message in self.extractor:
            message = parse_message(message)

            if isinstance(message, URLMessage):
                if message.url in self.visited:
                    continue
                else:
                    self.visited.add(message.url)

                downloader = Downloader(self.extractor)
                files.append(downloader.download(message.url, message.metadata))

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
                files = files + child_job.run()

            else:
                # We can probably ignore directory messages, they seem to just exist in order to
                # make sure the target directory exists for a file download.
                # Version messages are also not particularly meaningful for us.
                pass

        return files
