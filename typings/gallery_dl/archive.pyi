"""
This type stub file was generated by pyright.
"""

"""Download Archives"""

class DownloadArchive:
    def __init__(self, path, format_string, pragma=..., cache_key=...) -> None: ...
    def add(self, kwdict):  # -> None:
        """Add item described by 'kwdict' to archive"""
        ...

    def check(self, kwdict):  # -> Any:
        """Return True if the item described by 'kwdict' exists in archive"""
        ...

    def finalize(self):  # -> None:
        ...

class DownloadArchiveMemory(DownloadArchive):
    def __init__(self, path, format_string, pragma=..., cache_key=...) -> None: ...
    def add(self, kwdict):  # -> None:
        ...
    def check(self, kwdict):  # -> Any | Literal[True]:
        ...
    def finalize(self):  # -> None:
        ...
