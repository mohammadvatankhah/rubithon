from enum import auto

from .name_enum import NameEnum


class FileType(NameEnum):
    FILE = auto()
    GIF = auto()
    IMAGE = auto()
    MUSIC = auto()
    VIDEO = auto()
    VOICE = auto()
