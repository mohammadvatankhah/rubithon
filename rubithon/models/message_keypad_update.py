from typing import Optional

from rubithon import models
from .model import Model


class MessageKeypadUpdate(Model):

    def __init__(
        self,
        message_id: Optional[str] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.message_id = message_id
        self.inline_keypad = inline_keypad
