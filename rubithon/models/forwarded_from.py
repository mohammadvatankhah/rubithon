from typing import Optional

from rubithon import enums
from .model import Model


class ForwardedFrom(Model):

    def __init__(
        self,
        type_from: Optional["enums.ForwardedFromType"] = None,
        message_id: Optional[str] = None,
        from_chat_id: Optional[str] = None,
        from_sender_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.type_from = type_from
        self.message_id = message_id
        self.from_chat_id = from_chat_id
        self.from_sender_id = from_sender_id
