from ..models import Model
from .event_handler import EventHandler


class UpdateHandler(EventHandler):
    can_handle = Model

    def __init__(self, callback):
        super().__init__(callback)

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["update"] = event
        await super().handle(*args, **kwargs)
