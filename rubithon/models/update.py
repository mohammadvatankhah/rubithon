from typing import Optional

from rubithon import enums, models
from ..enums import UpdateType
from .chat import Chat
from .model import Model
from .removed_message import RemovedMessage


class Update(Model):
    attribute_names = [
        ("time", "update_time")
    ]

    def __init__(
        self,
        time: Optional[int] = None,
        type: Optional["enums.UpdateType"] = None,
        chat_id: Optional[str] = None,
        removed_message_id: Optional[str] = None,
        new_message: Optional["models.NewMessage"] = None,
        updated_message: Optional["models.UpdatedMessage"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.time = time
        self.type = type
        self.chat = Chat(id=chat_id) if chat_id else None

        self.removed_message = RemovedMessage(id=removed_message_id, time=time, chat=self.chat) if removed_message_id else None

        self.new_message = new_message 
        if new_message:
            self.new_message.chat = self.chat

        self.updated_message = updated_message
        if updated_message:
            self.updated_message.chat = self.chat

        if type == UpdateType.STARTED_BOT:
            self.__class__ = models.StartedBot
        elif type == UpdateType.STOPPED_BOT:
            self.__class__ = models.StoppedBot

    def get_effective_update(self):
        return self.new_message or self.updated_message or self.removed_message or self
