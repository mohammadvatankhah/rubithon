import rubithon


class DeleteMessage:

    async def delete_message(
        self: "rubithon.Client",
        chat_id: str,
        message_id: str
    ) -> bool:
        return await self._auto_execute("deleteMessage", locals())
