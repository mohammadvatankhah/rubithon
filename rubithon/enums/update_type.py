from enum import auto

from .name_enum import NameEnum


class UpdateType(NameEnum):
    NEW_MESSAGE = auto()
    REMOVED_MESSAGE = auto()
    STARTED_BOT = auto()
    STOPPED_BOT = auto()
    UPDATED_MESSAGE = auto()
    UPDATED_PAYMENT = auto()
