from pathlib import Path
from typing import List, Optional, Union

from rubithon import enums, models
from .model import Model


class Message(Model):
    attribute_names = [
        ("id", "message_id")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        text: Optional[str] = None,
        time: Optional[int] = None,
        is_edited: Optional[bool] = None,
        chat: Optional["models.Chat"] = None,
        sender_type: Optional["enums.MessageSenderType"] = None,
        sender_id: Optional[str] = None,
        aux_data: Optional["models.AuxData"] = None,
        file: Optional["models.File"] = None,
        reply_to_message_id: Optional[str] = None,
        forwarded_from: Optional["models.ForwardedFrom"] = None,
        forwarded_no_link: Optional[str] = None,
        location: Optional["models.Location"] = None,
        sticker: Optional["models.Sticker"] = None,
        contact_message: Optional["models.ContactMessage"] = None,
        poll: Optional["models.Poll"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.text = text
        self.time = time
        self.is_edited = is_edited
        self.chat = chat
        self.sender_type = sender_type
        self.sender_id = sender_id
        self.aux_data = aux_data
        self.file = file
        self.reply_to_message_id = reply_to_message_id
        self.forwarded_from = forwarded_from
        self.forwarded_no_link = forwarded_no_link
        self.location = location
        self.sticker = sticker
        self.contact_message = contact_message
        self.poll = poll

    async def delete(self):
        return await self.client.delete_message(
            self.chat.id,
            self.id
        )

    async def edit_keypad(
        self,
        keypad: "models.Keypad"
    ):
        return await self.client.edit_message_keypad(
            self.chat.id,
            self.id,
            keypad
        )

    async def edit_text(
        self,
        text: str
    ):
        return await self.client.edit_message_text(
            self.chat.id,
            self.id,
            text
        )

    async def forward(
        self,
        to_chat_id: str,
        disable_notification: bool = False
    ):
        return await self.client.forward_message(
            self.chat.id,
            self.id,
            to_chat_id,
            disable_notification
        )

    async def reply_contact(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        disable_notification: bool = False
    ):
        return await self.client.send_contact(
            self.chat.id,
            phone_number,
            first_name,
            last_name,
            inline_keypad,
            chat_keypad,
            chat_keypad_type,
            self.id,
            disable_notification
        )

    async def reply_location(
        self,
        latitude: str,
        longitude: str,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        disable_notification: bool = False
    ):
        return await self.client.send_location(
            self.chat.id,
            latitude,
            longitude,
            inline_keypad,
            chat_keypad,
            chat_keypad_type,
            self.id,
            disable_notification
        )

    async def reply_poll(
        self,
        question: str,
        options: List[str]
    ):
        return await self.client.send_poll(
            self.chat.id,
            question,
            options
        )

    async def reply_file(
        self,
        file: Union[str, Path, bytes],
        file_type: Optional["enums.FileType"] = enums.FileType.FILE,
        file_name: Optional[str] = None,
        text: Optional[str] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        disable_notification: bool = False
    ):
        return await self.client.send_file(
            self.chat.id,
            file,
            file_type,
            file_name,
            text,
            inline_keypad,
            chat_keypad,
            chat_keypad_type,
            self.id,
            disable_notification
        )

    async def reply(
        self,
        text: str,
        metadata: Optional["models.Metadata"] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        disable_notification: bool = False
    ):
        return await self.client.send_message(
            self.chat.id,
            text,
            metadata,
            inline_keypad,
            chat_keypad,
            chat_keypad_type,
            self.id,
            disable_notification
        )
