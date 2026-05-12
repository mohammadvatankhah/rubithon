from typing import Optional

import rubithon
from rubithon import enums, models


class EditChatKeypad:

    async def edit_chat_keypad(
        self: "rubithon.Client",
        chat_id: str,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: "enums.ChatKeypadType" = enums.ChatKeypadType.REMOVE
    ) -> bool:
        return await self._auto_execute("editChatKeypad", locals())
