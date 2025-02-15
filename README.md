# `gallery-dl-bytes`

[<img alt="UV Badge" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fuv%2Frefs%2Fheads%2Fmain%2Fassets%2Fbadge%2Fv0.json&style=for-the-badge">](https://docs.astral.sh/uv/)
[<img alt="Python Version Badge" src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fthcrt%2Fgallery-dl-bytes%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&style=for-the-badge">](#)
[<img alt="PyPI Downloads Badge" src="https://img.shields.io/pypi/dm/gallery-dl-bytes?style=for-the-badge&color=blue">](https://pypi.org/project/gallery-dl-bytes/)
[<img alt="License Badge" src="https://img.shields.io/pypi/l/gallery-dl-bytes?style=for-the-badge&color=blue">](./LICENSE)

[<img alt="Build Status Badge" src="https://img.shields.io/github/actions/workflow/status/thcrt/gallery-dl-bytes/publish.yml?event=release&style=for-the-badge">](https://github.com/thcrt/gallery-dl-bytes/actions/workflows/publish.yml)
[<img alt="Maintenance Status Badge" src="https://img.shields.io/maintenance/yes/2025?style=for-the-badge">](https://github.com/thcrt/gallery-dl-bytes/pulse)
[<img alt="Free Palestine Badge" src="https://img.shields.io/badge/Free%20-%20Palestine%20-%20red?style=for-the-badge">](https://bdsmovement.net/)

Programmatically run `gallery-dl` extractors to download content from the web directly to a `bytes` object in memory. With an easy, fully typed API.

<p align="center"><a href="https://github.com/thcrt/gallery-dl-bytes/"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" height="1em" width="1em" fill="currentcolor"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M64 0C28.7 0 0 28.7 0 64L0 448c0 35.3 28.7 64 64 64l256 0c35.3 0 64-28.7 64-64l0-288-128 0c-17.7 0-32-14.3-32-32L224 0 64 0zM256 0l0 128 128 0L256 0zM153 289l-31 31 31 31c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0L71 337c-9.4-9.4-9.4-24.6 0-33.9l48-48c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9zM265 255l48 48c9.4 9.4 9.4 24.6 0 33.9l-48 48c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l31-31-31-31c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0z"/></svg> <b>Source</b></a> | <a href="https://pypi.org/project/gallery-dl-bytes/"><svg viewBox="0 0 512 454" width="1em" height="1em" fill="currentcolor" xmlns="http://www.w3.org/2000/svg"><!-- PyPI icon from the File-Icons set - https://github.com/file-icons/icons/ --><path d="m454 305.8294373-91.1191101 33.691803v106.4807434l-180.9360199 65.9980163v-213.7029724l179.8842926-66.8633728v-172.609642l92.1708374 33.6728515zm-177.1609497 57.5555114c-15.7174377 5.7245483-28.4572144 23.9239502-28.4515686 40.6481018.0061646 16.7174377 12.7523499 25.6329346 28.4636841 19.919281 15.7173462-5.7247009 28.4602051-23.9217834 28.4544983-40.6459656-.0026551-16.7253112-12.749115-25.6428222-28.4666138-19.9214172zm57.7770386-150.8851623-180.3925323 66.8782959.2966461 135.7604065-64.2104874 22.9912415-90.3097153-32.8702699v-213.3329162l90.704361-33.6917877v-106.4804306l142.2673492-51.7543259 101.6443787 32.4636765zm-119.4016114-117.6667481c-15.7174835 5.7222672-28.4621582 23.9249802-28.458725 40.6499329.0025787 16.725235 12.750824 25.6462555 28.4683228 19.9248505 15.7174988-5.7219086 28.4623871-23.9248047 28.4592285-40.6498184-.0026397-16.7253037-12.7513275-25.64637-28.4688263-19.924965z"/></svg> <b>PyPI</b></a></p>


## Installation

### With `uv` (recommended)

```shell
uv add gallery-dl-bytes
```

### With `pip`

```shell
pip install gallery-dl-bytes
```

## Usage

### Single item

```python
from gallery_dl_bytes import DownloadJob

url = "https://www.reddit.com/r/me_irl/comments/1f4qc59/me_irl/"

job = DownloadJob(url)
job.run()
post = job.files[0]

print(f"{post.name}")
print(post.headers.get("Content-Type"))
print(post.metadata.get("author"))
```

### Gallery

```python
job = DownloadJob("https://imgur.com/gallery/dog-3s8hj1j")
job.run()

for file in job.files:
    print(f"{file.name}")
    print(file.headers.get("Last-Modified"))
    print(file.metadata.get("created_at"))
    print()
```

### Access media

```python
from pathlib import Path

job = DownloadJob("https://www.pexels.com/photo/man-riding-white-surfboard-1005456/")
job.run()

file = job.files[0]
Path(file.name).write_bytes(file.data)
```

### Access posts without media

```python
job = DownloadJob("https://bsky.app/profile/dril.bsky.social/post/3lia54f7fg22x")
job.run()

print(job.metadata.get("text"))
```

### Set `gallery-dl` configuration

> [!WARNING]  
> Note that not all configuration is supported. Options may be silently ignored. This feature is not yet complete.

```python
from gallery_dl_bytes import set_config

set_config(("extractor",), "browser", "firefox")
```
