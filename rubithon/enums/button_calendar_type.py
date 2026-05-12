from enum import auto

from .name_enum import NameEnum


class ButtonCalendarType(NameEnum):
    DATE = auto()
    DATETIME = auto()
