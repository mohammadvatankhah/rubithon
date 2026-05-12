import rubithon

from ..models import Chat


class GetChat:

    async def get_chat(
        self: "rubithon.Client",
        chat_id: str
    ) -> Chat:
        return await self._auto_execute("getChat", locals())
