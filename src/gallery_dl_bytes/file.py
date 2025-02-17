from dataclasses import dataclass, field
from pathlib import PurePath

from requests.models import CaseInsensitiveDict

from .extra_types import KWDict


@dataclass
class File:
    name: PurePath
    headers: CaseInsensitiveDict[str]
    metadata: KWDict
    data: bytes = field(repr=False)
