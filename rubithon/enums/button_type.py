from enum import auto

from .name_enum import NameEnum


class ButtonType(NameEnum):
    CALENDAR = auto()
    CALLBACK = auto()
    LOCATION = auto()
    NUMBER_PICKER = auto()
    SELECTION = auto()
    SIMPLE = auto()
    STRING_PICKER = auto()
    TEXT = auto()
    TEXTBOX = auto()
    URL = auto()
