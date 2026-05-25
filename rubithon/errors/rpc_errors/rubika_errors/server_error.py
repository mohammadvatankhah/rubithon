from .rubika_error import RubikaError


class ServerError(RubikaError):
    status = "SERVER_ERROR"
