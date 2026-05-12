from enum import auto

from .name_enum import NameEnum


class UpdateEndpointType(NameEnum):
    GET_SELECTION_ITEM = auto()
    RECEIVE_INLINE_MESSAGE = auto()
    RECEIVE_QUERY = auto()
    RECEIVE_UPDATE = auto()
    SEARCH_SELECTION_ITEMS = auto()
