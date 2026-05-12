from enum import auto

from .name_enum import NameEnum


class ButtonLocationType(NameEnum):
    PICKER = auto()
    VIEW = auto()
