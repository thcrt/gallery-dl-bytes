from gallery_dl.config import load as _load

from .job import DownloadJob as DownloadJob
from .util import set_config as set_config

_load()
del _load
