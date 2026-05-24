from typing import Optional

import rubithon
from rubithon import enums, models
from ..models import NewMessage


class SendContact:

    async def send_contact(
        self: "rubithon.Client",
        chat_id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> NewMessage:
        return await self._auto_execute("sendContact", locals())
