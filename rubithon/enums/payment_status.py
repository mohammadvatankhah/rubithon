from enum import auto

from .name_enum import NameEnum


class PaymentStatus(NameEnum):
    NOT_PAID = auto()
    PAID = auto()
