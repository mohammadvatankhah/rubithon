from typing import List

import rubithon

from ..models import NewMessage


class SendPoll:

    async def send_poll(
        self: "rubithon.Client",
        chat_id: str,
        question: str,
        options: List[str]
    ) -> NewMessage:
        return await self._auto_execute("sendPoll", locals())
