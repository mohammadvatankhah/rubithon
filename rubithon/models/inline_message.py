from typing import Optional

from rubithon import models

from .model import Model


class InlineMessage(Model):

    def __init__(
        self,
        sender_id: Optional[str] = None,
        text: Optional[str] = None,
        file: Optional["models.File"] = None,
        location: Optional["models.Location"] = None,
        aux_data: Optional["models.AuxData"] = None,
        message_id: Optional[str] = None,
        chat_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.sender_id = sender_id
        self.text = text
        self.file = file
        self.location = location
        self.aux_data = aux_data
        self.message_id = message_id
        self.chat_id = chat_id
