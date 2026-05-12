from enum import auto

from .name_enum import NameEnum


class MessageSenderType(NameEnum):
    BOT = auto()
    USER = auto()
