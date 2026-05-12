import rubithon


class BanChatMember:

    async def ban_chat_member(
        self: "rubithon.Client",
        chat_id: str,
        user_id: str
    ) -> bool:
        return await self._auto_execute("banChatMember", locals())
