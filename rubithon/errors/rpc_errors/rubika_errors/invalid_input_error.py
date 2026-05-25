from .rubika_error import RubikaError


class InvalidInputError(RubikaError):
    status = "INVALID_INPUT"
