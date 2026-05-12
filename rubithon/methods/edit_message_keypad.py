import rubithon
from rubithon import models


class EditMessageKeypad:

    async def edit_message_keypad(
        self: "rubithon.Client",
        chat_id: str,
        message_id: str,
        keypad: "models.Keypad"
    ) -> bool:
        return await self._auto_execute("editMessageKeypad", locals())
