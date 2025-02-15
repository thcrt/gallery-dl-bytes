"""
This type stub file was generated by pyright.
"""

import functools
import subprocess
import sys
from collections.abc import Iterable
from datetime import datetime
from typing import Callable, Type

from .extractor.common import Extractor

type KWDictValue = (
    str
    | int
    | float
    | bool
    | None
    | datetime
    | list[KWDictValue]
    | Type[Extractor]
    | KWDict
)
type KWDict = dict[str, KWDictValue]

"""Utility functions and classes"""

def bencode(num, alphabet=...):  # -> str:
    """Encode an integer into a base-N encoded string"""
    ...

def bdecode(data, alphabet=...):  # -> int:
    """Decode a base-N encoded string ( N = len(alphabet) )"""
    ...

def advance(iterable, num):
    """ "Advance 'iterable' by 'num' steps"""
    ...

def repeat(times):  # -> repeat[None]:
    """Return an iterator that returns None"""
    ...

def unique(iterable):  # -> Generator[Any, Any, None]:
    """Yield unique elements from 'iterable' while preserving order"""
    ...

def unique_sequence(iterable):  # -> Generator[Any, Any, None]:
    """Yield sequentially unique elements from 'iterable'"""
    ...

def contains(values, elements, separator=...):  # -> bool:
    """Returns True if at least one of 'elements' is contained in 'values'"""
    ...

def raises(cls):  # -> Callable[..., NoReturn]:
    """Returns a function that raises 'cls' as exception"""
    ...

def identity(x, _=...):
    """Returns its argument"""
    ...

def true(_, __=...):  # -> Literal[True]:
    """Always returns True"""
    ...

def false(_, __=...):  # -> Literal[False]:
    """Always returns False"""
    ...

def noop():  # -> None:
    """Does nothing"""
    ...

def md5(s):  # -> str:
    """Generate MD5 hexdigest of 's'"""
    ...

def sha1(s):  # -> str:
    """Generate SHA1 hexdigest of 's'"""
    ...

def generate_token(size=...):  # -> str:
    """Generate a random token with hexadecimal digits"""
    ...

def format_value(value, suffixes=...):  # -> str:
    ...
def combine_dict(a, b):
    """Recursively combine the contents of 'b' into 'a'"""
    ...

def transform_dict(a, func):  # -> None:
    """Recursively apply 'func' to all values in 'a'"""
    ...

def filter_dict(a):  # -> dict[Any, Any]:
    """Return a copy of 'a' without "private" entries"""
    ...

def delete_items(obj, keys):  # -> None:
    """Remove all 'keys' from 'obj'"""
    ...

def enumerate_reversed(
    iterable, start=..., length=...
):  # -> zip[tuple[int, Any]] | list[tuple[int, Any]]:
    """Enumerate 'iterable' and return its elements in reverse order"""
    ...

def number_to_string(value, numbers=...):  # -> str:
    """Convert numbers (int, float) to string; Return everything else as is."""
    ...

def to_string(value):  # -> str:
    """str() with "better" defaults"""
    ...

def datetime_to_timestamp(dt):
    """Convert naive UTC datetime to Unix timestamp"""
    ...

def datetime_to_timestamp_string(dt):  # -> str:
    """Convert naive UTC datetime to Unix timestamp string"""
    ...

if sys.hexversion < 51118080:
    datetime_utcfromtimestamp = ...
    datetime_utcnow = ...
    datetime_from_timestamp = ...
else:
    def datetime_from_timestamp(ts=...):  # -> datetime:
        """Convert Unix timestamp to naive UTC datetime"""
        ...

    datetime_utcfromtimestamp = ...
    datetime_utcnow = ...

def json_default(obj):  # -> str | None:
    ...

json_loads = ...
json_dumps = ...

def dump_json(obj, fp=..., ensure_ascii=..., indent=...):  # -> None:
    """Serialize 'obj' as JSON and write it to 'fp'"""
    ...

def dump_response(response, fp, headers=..., content=..., hide_auth=...):  # -> None:
    """Write the contents of 'response' into a file-like object"""
    ...

def extract_headers(response):  # -> dict[Any, Any]:
    ...
@functools.cache
def git_head():  # -> None:
    ...
def expand_path(path):  # -> str:
    """Expand environment variables and tildes (~)"""
    ...

def remove_file(path):  # -> None:
    ...
def remove_directory(path):  # -> None:
    ...
def set_mtime(path, mtime):  # -> None:
    ...
def cookiestxt_load(fp):  # -> list[Any]:
    """Parse a Netscape cookies.txt file and add return its Cookies"""
    ...

def cookiestxt_store(fp, cookies):  # -> None:
    """Write 'cookies' in Netscape cookies.txt format to 'fp'"""
    ...

def code_to_language(code, default=...):  # -> str | None:
    """Map an ISO 639-1 language code to its actual name"""
    ...

def language_to_code(lang, default=...):  # -> str | None:
    """Map a language name to its ISO 639-1 code"""
    ...

CODES = ...

class HTTPBasicAuth:
    __slots__ = ...
    def __init__(self, username, password) -> None: ...
    def __call__(self, request): ...

class ModuleProxy:
    __slots__ = ...
    def __getitem__(self, key, modules=...):  # -> CustomNone:
        ...

    __getattr__ = ...

class LazyPrompt:
    __slots__ = ...
    def __str__(self) -> str: ...

class NullContext:
    __slots__ = ...
    def __enter__(self):  # -> None:
        ...
    def __exit__(self, exc_type, exc_value, traceback):  # -> None:
        ...

class CustomNone:
    """None-style type that supports more operations than regular None"""

    __slots__ = ...
    __getattribute__ = ...
    __getitem__ = ...
    __iter__ = ...
    def __call__(self, *args, **kwargs):  # -> Self:
        ...
    @staticmethod
    def __next__(): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

    __lt__ = ...
    __le__ = ...
    __gt__ = ...
    __ge__ = ...
    __bool__ = ...
    __add__ = ...
    __sub__ = ...
    __mul__ = ...
    __matmul__ = ...
    __truediv__ = ...
    __floordiv__ = ...
    __mod__ = ...
    __radd__ = ...
    __rsub__ = ...
    __rmul__ = ...
    __rmatmul__ = ...
    __rtruediv__ = ...
    __rfloordiv__ = ...
    __rmod__ = ...
    __lshift__ = ...
    __rshift__ = ...
    __and__ = ...
    __xor__ = ...
    __or__ = ...
    __rlshift__ = ...
    __rrshift__ = ...
    __rand__ = ...
    __rxor__ = ...
    __ror__ = ...
    __neg__ = ...
    __pos__ = ...
    __abs__ = ...
    __invert__ = ...
    @staticmethod
    def __len__():  # -> Literal[0]:
        ...

    __int__ = ...
    __hash__ = ...
    __index__ = ...
    @staticmethod
    def __format__(_):  # -> Literal['None']:
        ...
    @staticmethod
    def __str__() -> str: ...

    __repr__ = ...

_ff_ver = ...
NONE = ...
EPOCH = ...
SECOND = ...
WINDOWS = ...
SENTINEL = ...
EXECUTABLE = ...
USERAGENT = ...
USERAGENT_FIREFOX = ...
SPECIAL_EXTRACTORS = ...
GLOBALS = ...
if EXECUTABLE and hasattr(sys, "_MEIPASS"):
    _popen_env = ...
    orig = ...
    orig = ...
    class Popen(subprocess.Popen):
        def __init__(self, args, **kwargs) -> None: ...

else:
    Popen = ...

def compile_expression_raw(expr, name=..., globals=...):  # -> partial[Any]:
    ...
def compile_expression_defaultdict(expr, name=..., globals=...):  # -> partial[Any]:
    ...
def compile_expression_defaultdict_impl(
    expr, name=..., globals=...
):  # -> partial[Any]:
    ...
def compile_expression_tryexcept(
    expr, name=..., globals=...
):  # -> Callable[..., Any | CustomNone]:
    ...

compile_expression = ...

def compile_filter(expr, name=..., globals=...):  # -> Callable[..., Any | CustomNone]:
    ...
def import_file(path):  # -> Any:
    """Import a Python module from a filesystem path"""
    ...

def build_duration_func(
    duration, min=...
):  # -> Callable[[], float] | partial[float] | Callable[[], float | Any] | None:
    ...
def build_extractor_filter(
    categories: Iterable[str] | str, negate: bool = ..., special: set[str] | None = ...
) -> Callable[[Extractor], bool]:
    """Build a function that takes an Extractor class as argument
    and returns True if that class is allowed by 'categories'
    """
    ...

def build_proxy_map(proxies, log=...):  # -> dict[str, str] | dict[Any, Any] | None:
    """Generate a proxy map"""
    ...

def build_predicate(predicates):  # -> Callable[..., Literal[True]] | partial[bool]:
    ...
def chain_predicates(predicates, url, kwdict):  # -> bool:
    ...

class RangePredicate:
    """Predicate; True if the current index is in the given range(s)"""
    def __init__(self, rangespec) -> None: ...
    def __call__(self, _url, _kwdict):  # -> bool:
        ...

class UniquePredicate:
    """Predicate; True if given URL has not been encountered before"""
    def __init__(self) -> None: ...
    def __call__(self, url, _):  # -> bool:
        ...

class FilterPredicate:
    """Predicate; True if evaluating the given expression returns True"""
    def __init__(self, expr, target=...) -> None: ...
    def __call__(self, _, kwdict):  # -> Any | CustomNone:
        ...
