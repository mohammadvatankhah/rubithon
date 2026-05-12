from ..models import StartedBot
from .update_handler import UpdateHandler


class StartedBotHandler(UpdateHandler):
    can_handle = StartedBot

    def __init__(self, callback):
        super().__init__(callback)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["started_bot"] = event
        return super().handle(*args, **kwargs)
