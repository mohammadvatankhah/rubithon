from enum import auto

from .name_enum import NameEnum


class LiveLocationStatus(NameEnum):
    LIVE = auto()
    STOPPED = auto()
