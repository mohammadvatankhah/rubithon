from enum import auto

from .name_enum import NameEnum


class ForwardedFromType(NameEnum):
    BOT = auto()
    CHANNEL = auto()
    USER = auto()
