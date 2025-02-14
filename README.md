# `gallery-dl-bytes`

Programmatically run `gallery-dl` extractors to download content from the web.

## Usage

### Single item

```python
from gallery_dl_bytes import download

url = "https://www.reddit.com/r/me_irl/comments/1f4qc59/me_irl/"

files = download(url)                       # returns a list of File objects
post = files[0]                             # this post only has one image

print(f"{post.name}")                       # 1f4qc59 me_irl.jpeg
print(post.headers.get("Content-Type"))     # image/jpeg
print(post.metadata.get("author"))          # DevianceSX
```

### Gallery

```python
from gallery_dl_bytes import download

url = "https://imgur.com/gallery/dog-3s8hj1j"

files = download(url)

for file in files:
    print(f"{file.name}")
    print(file.headers.get("Last-Modified"))
    print(file.metadata.get("created_at"))
    print()

    # None_3s8hj1j_001_QQzDgCw.jpg
    # Tue, 29 Dec 2020 19:32:52 GMT
    # 2020-12-29T19:32:50Z

    # None_3s8hj1j_002_StcxXhO.jpg
    # Tue, 29 Dec 2020 19:32:55 GMT
    # 2020-12-29T19:32:54Z

    # None_3s8hj1j_003_sbzwzqH.jpg
    # Tue, 29 Dec 2020 19:32:58 GMT
    # 2020-12-29T19:32:57Z
```

### Access media

```python
from pathlib import Path
from gallery_dl_bytes import download

file = download("https://unsplash.com/photos/qQ6s9iqLVow")[0]
Path(file.name).write_bytes(file.data)
```