from pathlib import Path
from typing import Optional, Union

import rubithon
from rubithon import enums, models
from ..models import NewMessage


class SendFile:

    async def send_file(
        self: "rubithon.Client",
        chat_id: str,
        file_id: Optional[str] = None,
        file: Optional[Union[str, Path, bytes]] = None,
        file_type: Optional["enums.FileType"] = enums.FileType.FILE,
        file_name: Optional[str] = None,
        text: Optional[str] = None,
        inline_keypad: Optional["models.Keypad"] = None,
        chat_keypad: Optional["models.Keypad"] = None,
        chat_keypad_type: Optional["enums.ChatKeypadType"] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> NewMessage:
        if file_id is None:
            if file is None:
                raise ValueError("Either \"file_id\" or \"file\" must be provided")
            file_id = await self.upload(file, file_name, file_type)

        del file
        del file_type
        del file_name

        return await self._auto_execute("sendFile", locals())
