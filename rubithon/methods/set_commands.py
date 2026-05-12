from typing import List

import rubithon
from rubithon import models


class SetCommands:

    async def set_commands(
        self: "rubithon.Client",
        bot_commands: List["models.BotCommand"]
    ) -> bool:
        return await self._auto_execute("setCommands", locals())
