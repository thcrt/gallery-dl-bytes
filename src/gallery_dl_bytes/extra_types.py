from datetime import datetime
from typing import TYPE_CHECKING, Literal

from gallery_dl.extractor.common import Extractor

type KWDictValue = (
    str | int | float | bool | None | datetime | list[KWDictValue] | type[Extractor] | KWDict
)
type KWDict = dict[str, KWDictValue]

type VersionMessage = tuple[
    Literal[1],
    int,
]
type DirectoryMessage = tuple[
    Literal[2],
    KWDict,
]
type URLMessage = tuple[
    Literal[3],
    str,
    KWDict,
]
type QueueMessage = tuple[
    Literal[6],
    str,
    KWDict,
]

type MessageType = VersionMessage | DirectoryMessage | URLMessage | QueueMessage


if TYPE_CHECKING:
    from gallery_dl.extractor.message import MessageType as MessageType  # type: ignore
    from gallery_dl.util import KWDict as KWDict  # type: ignore
