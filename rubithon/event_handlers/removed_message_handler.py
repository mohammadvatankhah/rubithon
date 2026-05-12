from ..models import RemovedMessage
from .update_handler import UpdateHandler


class RemovedMessageHandler(UpdateHandler):
    can_handle = RemovedMessage

    def __init__(self, callback):
        super().__init__(callback)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["message"] = event
        return super().handle(*args, **kwargs)
