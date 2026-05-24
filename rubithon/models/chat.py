from typing import Optional

from rubithon import enums, models
from .model import Model


class Chat(Model):
    attribute_names = [
        ("id", "chat_id"),
        ("type", "chat_type")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional["enums.ChatType"] = None,
        user_id: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        title: Optional[str] = None,
        username: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.type = type
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.username = username

    async def edit_keypad(
        self,
        keypad: Optional["models.Keypad"] = None,
        keypad_type: "enums.ChatKeypadType" = enums.ChatKeypadType.REMOVE
    ):
        return await self.client.edit_chat_keypad(
            self.id,
            keypad,
            keypad_type
        )

    async def get(self):
        return await self.client.get_chat(self.id)

    async def ban_member(
        self,
        user_id: str
    ):
        return await self.client.ban_chat_member(
            self.id,
            user_id
        )

    async def unban_member(
        self,
        user_id: str
    ):
        return await self.client.unban_chat_member(
            self.id,
            user_id
        )
