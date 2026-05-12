from enum import auto

from .name_enum import NameEnum


class ChatType(NameEnum):
    BOT = auto()
    CHANNEL = auto()
    GROUP = auto()
    USER = auto()
