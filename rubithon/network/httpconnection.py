import logging
import ssl
from io import BytesIO
from pathlib import Path
from typing import Optional, Union

import aiohttp

from ..errors import RPCError

log = logging.getLogger(__name__)


class HTTPConnection:
    BASE_URL = "https://botapi.rubika.ir/v3"
    TIMEOUT = 20

    def __init__(
        self,
        token: str,
        timeout: Optional[int] = None,
        proxy: Optional[str] = None,
        base_url: Optional[str] = None
    ):
        self.token = token
        self.timeout = timeout or self.TIMEOUT
        self.proxy = proxy
        self.base_url = (base_url or self.BASE_URL).rstrip("/")

        self.client: Optional["aiohttp.ClientSession"] = None
        self.is_started = False

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")

        self.is_started = True

        connector = aiohttp.TCPConnector(ssl=ssl.create_default_context())
        timeout = aiohttp.ClientTimeout(total=self.timeout)
        self.client = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers={"Content-Type": "application/json"},
        )

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")

        self.is_started = False

        if self.client and not self.client.closed:
            await self.client.close()
            self.client = None

    def _get_bot_url(self):
        return f"{self.base_url}/{self.token}"

    async def request(self, service: str, json: dict):
        url = f"{self._get_bot_url()}/{service}"

        log.info(f"[{service}] JSON: {json}")

        response = await self.client.post(url, json=json)
        response_json = await response.json()

        status = response_json.get("status")
        if status != "OK":
            dev_message = response_json.get("dev_message")
            raise RPCError.create(status, dev_message, service)

        return response_json.get("data")

    async def download_file(self, url: str):
        buffer = BytesIO()

        async with self.client.get(url) as response:
            response.raise_for_status()
            async for chunk in response.content.iter_chunked(8_192):
                buffer.write(chunk)

        return buffer.getvalue()

    async def upload_file(
        self,
        url: str,
        file: Union[str, Path, bytes],
        file_name: Optional[str] = None
    ) -> str:
        if file_name is None:
            file_name = Path(file).name if isinstance(file, (str, Path)) else "file"

        if isinstance(file, (str, Path)):
            with open(file, "rb") as f:
                file = f.read()

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
            filename=file_name,
            content_type="application/octet-stream"
        )

        async with self.client.post(url, data=form) as response:
            response.raise_for_status()
            result = await response.json()

        return result.get("file_id")
