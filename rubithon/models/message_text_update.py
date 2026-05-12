from typing import Optional

from .model import Model


class MessageTextUpdate(Model):

    def __init__(
        self,
        message_id: Optional[str] = None,
        text: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.message_id = message_id
        self.text = text
