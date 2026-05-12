import rubithon
from rubithon import enums


class UpdateBotEndpoints:

    async def update_bot_endpoints(
        self: "rubithon.Client",
        url: str,
        type: "enums.UpdateEndpointType" = enums.UpdateEndpointType.RECEIVE_UPDATE
    ) -> bool:
        return await self._auto_execute("updateBotEndpoints", locals())
