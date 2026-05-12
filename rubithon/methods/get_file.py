import rubithon


class GetFile:

    async def get_file(
        self: "rubithon.Client",
        file_id: str
    ) -> str:
        result = await self._auto_execute("getFile", locals())
        return result.get("download_url")
