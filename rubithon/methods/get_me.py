import rubithon

from ..models import Bot


class GetMe:

    async def get_me(self: "rubithon.Client") -> Bot:
        return await self._auto_execute("getMe", locals())
