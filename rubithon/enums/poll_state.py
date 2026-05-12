from enum import auto

from .name_enum import NameEnum


class PollState(NameEnum):
    CLOSED = auto()
    OPEN = auto()
