from .rubika_error import RubikaError


class TooRequestsError(RubikaError):
    status = "TOO_REQUESTS"
