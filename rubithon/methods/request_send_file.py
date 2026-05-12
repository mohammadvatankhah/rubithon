import rubithon
from rubithon import enums


class RequestSendFile:

    async def request_send_file(
        self: "rubithon.Client",
        type: "enums.FileType" = enums.FileType.FILE
    ) -> str:
        result = await self._auto_execute("requestSendFile", locals())
        return result.get("upload_url")
