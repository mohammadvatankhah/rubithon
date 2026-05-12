from typing import Optional

import rubithon
from rubithon import enums, models

from ..models import NewMessage


class SendMessage:

    async def send_message(
        self: "rubithon.Client",
        chat_id: str,
        text: str,
        metadata: Optional["models.Metadata"] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> NewMessage:
        return await self._auto_execute("sendMessage", locals())
