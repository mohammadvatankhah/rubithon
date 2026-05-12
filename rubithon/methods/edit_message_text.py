import rubithon


class EditMessageText:

    async def edit_message_text(
        self: "rubithon.Client",
        chat_id: str,
        message_id: str,
        text: str
    ) -> bool:
        return await self._auto_execute("editMessageText", locals())
