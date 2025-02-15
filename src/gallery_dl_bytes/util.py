from collections.abc import Callable, Collection
from typing import Any

from gallery_dl.config import set as _set_config


def set_config(path: Collection[str], key: str, value: Any) -> None:
    _set_config(path, key, value)


MIME_TYPES = {
    "image/jpeg": "jpg",
    "image/jpg": "jpg",
    "image/png": "png",
    "image/gif": "gif",
    "image/bmp": "bmp",
    "image/x-bmp": "bmp",
    "image/x-ms-bmp": "bmp",
    "image/webp": "webp",
    "image/avif": "avif",
    "image/heic": "heic",
    "image/heif": "heif",
    "image/svg+xml": "svg",
    "image/ico": "ico",
    "image/icon": "ico",
    "image/x-icon": "ico",
    "image/vnd.microsoft.icon": "ico",
    "image/x-photoshop": "psd",
    "application/x-photoshop": "psd",
    "image/vnd.adobe.photoshop": "psd",
    "video/webm": "webm",
    "video/ogg": "ogg",
    "video/mp4": "mp4",
    "video/m4v": "m4v",
    "video/x-m4v": "m4v",
    "video/quicktime": "mov",
    "audio/wav": "wav",
    "audio/x-wav": "wav",
    "audio/webm": "webm",
    "audio/ogg": "ogg",
    "audio/mpeg": "mp3",
    "application/zip": "zip",
    "application/x-zip": "zip",
    "application/x-zip-compressed": "zip",
    "application/rar": "rar",
    "application/x-rar": "rar",
    "application/x-rar-compressed": "rar",
    "application/x-7z-compressed": "7z",
    "application/pdf": "pdf",
    "application/x-pdf": "pdf",
    "application/x-shockwave-flash": "swf",
    "application/ogg": "ogg",
    # https://www.iana.org/assignments/media-types/model/obj
    "model/obj": "obj",
    "application/octet-stream": "bin",
}

# https://en.wikipedia.org/wiki/List_of_file_signatures
SIGNATURE_CHECKS: dict[str, Callable[[bytes], bool]] = {
    "jpg": lambda s: s[0:3] == b"\xff\xd8\xff",
    "png": lambda s: s[0:8] == b"\x89PNG\r\n\x1a\n",
    "gif": lambda s: s[0:6] in (b"GIF87a", b"GIF89a"),
    "bmp": lambda s: s[0:2] == b"BM",
    "webp": lambda s: (s[0:4] == b"RIFF" and s[8:12] == b"WEBP"),
    "avif": lambda s: s[4:11] == b"ftypavi" and s[11] in b"fs",
    "heic": lambda s: (
        s[4:10] == b"ftyphe" and s[10:12] in (b"ic", b"im", b"is", b"ix", b"vc", b"vm", b"vs")
    ),
    "svg": lambda s: s[0:5] == b"<?xml",
    "ico": lambda s: s[0:4] == b"\x00\x00\x01\x00",
    "cur": lambda s: s[0:4] == b"\x00\x00\x02\x00",
    "psd": lambda s: s[0:4] == b"8BPS",
    "mp4": lambda s: (s[4:8] == b"ftyp" and s[8:11] in (b"mp4", b"avc", b"iso")),
    "m4v": lambda s: s[4:11] == b"ftypM4V",
    "mov": lambda s: s[4:12] == b"ftypqt  ",
    "webm": lambda s: s[0:4] == b"\x1a\x45\xdf\xa3",
    "ogg": lambda s: s[0:4] == b"OggS",
    "wav": lambda s: (s[0:4] == b"RIFF" and s[8:12] == b"WAVE"),
    "mp3": lambda s: (s[0:3] == b"ID3" or s[0:2] in (b"\xff\xfb", b"\xff\xf3", b"\xff\xf2")),
    "zip": lambda s: s[0:4] in (b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08"),
    "rar": lambda s: s[0:6] == b"Rar!\x1a\x07",
    "7z": lambda s: s[0:6] == b"\x37\x7a\xbc\xaf\x27\x1c",
    "pdf": lambda s: s[0:5] == b"%PDF-",
    "swf": lambda s: s[0:3] in (b"CWS", b"FWS"),
    "blend": lambda s: s[0:7] == b"BLENDER",
    # unfortunately the Wavefront .obj format doesn't have a signature,
    # so we check for the existence of Blender's comment
    "obj": lambda s: s[0:11] == b"# Blender v",
    # Celsys Clip Studio Paint format
    # https://github.com/rasensuihei/cliputils/blob/master/README.md
    "clip": lambda s: s[0:8] == b"CSFCHUNK",
    # check 'bin' files against all other file signatures
    "bin": lambda s: False,
}
