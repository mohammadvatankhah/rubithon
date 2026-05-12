import rubithon

from ..models import Message


class ForwardMessage:

    async def forward_message(
        self: "rubithon.Client",
        from_chat_id: str,
        message_id: str,
        to_chat_id: str,
        disable_notification: bool = False
    ) -> Message:
        return await self._auto_execute("forwardMessage", locals())
