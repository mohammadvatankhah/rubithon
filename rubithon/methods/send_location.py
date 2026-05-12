from typing import Optional

import rubithon
from rubithon import enums, models

from ..models import NewMessage


class SendLocation:

    async def send_location(
        self: "rubithon.Client",
        chat_id: str,
        latitude: str,
        longitude: str,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> NewMessage:
        return await self.auto_execute("sendLocation", locals())
