import rubithon


class UnbanChatMember:

    async def unban_chat_member(
        self: "rubithon.Client",
        chat_id: str,
        user_id: str
    ) -> bool:
        return await self._auto_execute("unbanChatMember", locals())
