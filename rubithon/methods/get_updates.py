from typing import Optional

import rubithon

from ..models import Updates


class GetUpdates:

    async def get_updates(
        self: "rubithon.Client",
        offset_id: Optional[str] = None,
        limit: Optional[int] = None
    ) -> Updates:
        return await self._auto_execute("getUpdates", locals())
