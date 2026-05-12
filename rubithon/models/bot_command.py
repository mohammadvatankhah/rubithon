from .model import Model


class BotCommand(Model):

    def __init__(
        self,
        command: str,
        description: str,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.command = command
        self.description = description
