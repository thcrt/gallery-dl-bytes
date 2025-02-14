from dataclasses import dataclass, field
from pathlib import PurePath
from typing import TYPE_CHECKING

from requests.models import CaseInsensitiveDict

if TYPE_CHECKING:
    from gallery_dl.util import KWDict


@dataclass
class File:
    name: PurePath
    headers: CaseInsensitiveDict[str]
    metadata: "KWDict"
    data: bytes = field(repr=False)
