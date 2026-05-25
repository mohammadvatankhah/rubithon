from .rubika_error import RubikaError


class InvalidAccessError(RubikaError):
    status = "INVALID_ACCESS"
