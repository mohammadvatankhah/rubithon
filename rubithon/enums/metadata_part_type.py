from enum import auto

from .name_enum import NameEnum


class MetadataPartType(NameEnum):
    BOLD = auto()
    ITALIC = auto()
    LINK = auto()
    MENTION_TEXT = auto()
    MONO = auto()
    PRE = auto()
    QUOTE = auto()
    SPOILER = auto()
    STRIKE = auto()
    UNDERLINE = auto()
