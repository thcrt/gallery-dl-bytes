"""
This type stub file was generated by pyright.
"""

import sys

"""Collection of functions that work on strings/text"""
HTML_RE = ...

def remove_html(txt, repl=..., sep=...):  # -> str:
    """Remove html-tags from a string"""
    ...

def split_html(txt):  # -> list[str | Any] | list[Any]:
    """Split input string by HTML tags"""
    ...

def slugify(value):  # -> str:
    """Convert a string to a URL slug

    Adapted from:
    https://github.com/django/django/blob/master/django/utils/text.py
    """
    ...

def ensure_http_scheme(url, scheme=...):
    """Prepend 'scheme' to 'url' if it doesn't have one"""
    ...

def root_from_url(url, scheme=...):
    """Extract scheme and domain from a URL"""
    ...

def filename_from_url(url):  # -> Literal['']:
    """Extract the last part of an URL to use as a filename"""
    ...

def ext_from_url(url):  # -> LiteralString | Literal['']:
    """Extract the filename extension of an URL"""
    ...

def nameext_from_url(url, data=...):  # -> dict[Any, Any]:
    """Extract the last part of an URL and fill 'data' accordingly"""
    ...

def extract(txt, begin, end, pos=...):  # -> tuple[Any, Any] | tuple[None, int]:
    """Extract the text between 'begin' and 'end' from 'txt'

    Args:
        txt: String to search in
        begin: First string to be searched for
        end: Second string to be searched for after 'begin'
        pos: Starting position for searches in 'txt'

    Returns:
        The string between the two search-strings 'begin' and 'end' beginning
        with position 'pos' in 'txt' as well as the position after 'end'.

        If at least one of 'begin' or 'end' is not found, None and the original
        value of 'pos' is returned

    Examples:
        extract("abcde", "b", "d")    -> "c" , 4
        extract("abcde", "b", "d", 3) -> None, 3
    """
    ...

def extr(txt, begin, end, default=...):  # -> str:
    """Stripped-down version of 'extract()'"""
    ...

def rextract(txt, begin, end, pos=...):  # -> tuple[Any, Any] | tuple[None, int]:
    ...
def extract_all(
    txt, rules, pos=..., values=...
):  # -> tuple[Any | dict[Any, Any], int | Any]:
    """Calls extract for each rule and returns the result in a dict"""
    ...

def extract_iter(txt, begin, end, pos=...):  # -> Generator[Any, Any, None]:
    """Yield values that would be returned by repeated calls of extract()"""
    ...

def extract_from(txt, pos=..., default=...):  # -> Callable[..., Any | str]:
    """Returns a function object that extracts from 'txt'"""
    ...

def parse_unicode_escapes(txt):  # -> str:
    """Convert JSON Unicode escapes in 'txt' into actual characters"""
    ...

def parse_bytes(value: str, default: int = ..., suffixes: str = ...) -> int:
    """Convert a bytes-amount ("500k", "2.5M", ...) to int"""
    ...

def parse_int(value, default=...):  # -> int:
    """Convert 'value' to int"""
    ...

def parse_float(value, default=...):  # -> float:
    """Convert 'value' to float"""
    ...

def parse_query(qs):  # -> dict[Any, Any]:
    """Parse a query string into name-value pairs

    Ignore values whose name has been seen before
    """
    ...

def parse_query_list(qs):  # -> dict[Any, Any]:
    """Parse a query string into name-value pairs

    Combine values of duplicate names into lists
    """
    ...

if sys.hexversion < 51118080:
    def parse_timestamp(ts, default=...):  # -> datetime | None:
        """Create a datetime object from a Unix timestamp"""
        ...

else:
    def parse_timestamp(ts, default=...):  # -> datetime | None:
        """Create a datetime object from a Unix timestamp"""
        ...

def parse_datetime(date_string, format=..., utcoffset=...):  # -> datetime | None:
    """Create a datetime object by parsing 'date_string'"""
    ...

urljoin = ...
quote = ...
unquote = ...
escape = ...
unescape = ...
