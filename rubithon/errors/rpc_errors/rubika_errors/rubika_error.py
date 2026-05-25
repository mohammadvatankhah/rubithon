from typing import Optional

from ..rpc_error import RPCError


class RubikaError(RPCError):
    status: Optional[str] = None

    @classmethod
    def create(
        cls,
        status: Optional[str] = None,
        dev_message: Optional[str] = None,
        reason: Optional[str] = None
    ):
        for rpc_error in cls.__subclasses__():
            if status == rpc_error.status:
                return rpc_error(status, dev_message, reason)

        return cls(status, dev_message, reason)

    def __init__(
        self,
        status: Optional[str] = None,
        dev_message: Optional[str] = None,
        reason: Optional[str] = None
    ):
        self.status = status
        self.dev_message = dev_message
        self.reason = reason
        super().__init__(str(self))

    def __str__(self):
        status = "" if self.status is None else f"{self.status}"
        dev_message = "" if self.dev_message is None else f": {self.dev_message}"
        reason = "" if self.reason is None else f" (caused by {self.reason})"
        return f"{status}{dev_message}{reason}"
