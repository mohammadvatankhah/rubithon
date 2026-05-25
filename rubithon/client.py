import asyncio
from inspect import iscoroutine, iscoroutinefunction, stack
from pathlib import Path
from typing import (
    Any,
    Callable,
    Coroutine,
    Optional,
    Union,
    get_type_hints
)
from time import time

import aiohttp

from rubithon import enums, models
from .dispatcher import Chain, Dispatcher, PrintingChain
from .errors import TooRequestsError
from .event_handlers import (
    ConnectHandler,
    DisconnectHandler,
    InitializeHandler,
    ShutdownHandler
)
from .methods import Methods
from .models import Model, unwrap, wrap
from .network import HTTPConnection


class Client(Chain, Methods):

    def __init__(
        self,
        token: str,
        timeout: Optional[int] = None,
        proxy: Optional[str] = None,
        base_url: Optional[str] = None,
        retry_delay: int = 60,
        max_retries: int = 3,
        async_workers: Optional[int] = None
    ):
        super().__init__("default", PrintingChain())
        self.token = token
        self.timeout = timeout
        self.proxy = proxy
        self.base_url = base_url
        self.retry_delay = retry_delay
        self.max_retries = max_retries

        self.bot: Optional["models.Bot"] = None
        self.dispatcher = Dispatcher(self, async_workers)
        self._is_disconnected = False
        self._http_connection = HTTPConnection(token, timeout, proxy, base_url)
        self._next_offset_id: Optional[str] = None
        self._last_update_time: Optional[int] = None

    def __repr__(self):
        client_name = type(self).__name__
        try:
            name = self.bot.title
        except AttributeError:
            name = "Not initialized yet"
        return f"{client_name}({name})"

    async def connect(self):
        await self._http_connection.start()
        self.bot = await self.get_me()

    async def disconnect(self):
        await self._http_connection.stop()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        try:
            await self.disconnect()
        except ConnectionError:
            return

    async def initialize(self):
        await self.dispatcher.start()
        await self.dispatcher.dispatch_event(self, InitializeHandler)

    async def shutdown(self):
        await self.dispatcher.dispatch_event(self, ShutdownHandler)
        await self.dispatcher.stop()

    async def _execute(
        self,
        service: str,
        **data
    ):
        data = {k: v for k, v in data.items() if v is not None}

        for key, value in data.items():
            data[key] = unwrap(value)

        retries = 0
        while retries <= self.max_retries:
            try:
                return await self._http_connection.request(service, json=data)
            except TooRequestsError as error:
                retries += 1
                if retries > self.max_retries:
                    raise error
                await asyncio.sleep(self.retry_delay)

    async def _auto_execute(
        self,
        service: str,
        data: dict
    ):
        bound_method_name = stack()[1].function
        bound_method = getattr(self, bound_method_name)
        type_hints = get_type_hints(bound_method)
        del data["self"]
        del type_hints["self"]
        return_type_hint = type_hints.pop("return")

        result = await self._execute(service, **data)

        if return_type_hint is bool:
            return True

        result = wrap(return_type_hint, result)
        if isinstance(result, Model):
            result.bind(self)
        return result

    async def _start_polling(self, clear_pending_updates: bool = True):
        await self.initialize()

        start_time = time()

        while True:
            try:
                result = await self.get_updates(offset_id=self._next_offset_id)
            except aiohttp.ClientConnectorError:
                if not self._is_disconnected:
                    self._is_disconnected = True
                    await self.dispatcher.dispatch_event(self, DisconnectHandler)
                continue
            except Exception as error:
                await self.dispatcher.dispatch_event(self, error)
                continue

            if self._is_disconnected:
                self._is_disconnected = False
                await self.dispatcher.dispatch_event(self, ConnectHandler)

            if self._next_offset_id is None:
                if clear_pending_updates:
                    self._next_offset_id = result.next_offset_id
                    continue

            for update in result.updates:
                if (
                    clear_pending_updates
                    and update.time is not None
                    and update.time < start_time
                ):
                    continue

                if (
                    self._last_update_time is not None
                    and update.time is not None
                    and update.time <= self._last_update_time
                ):
                    continue

                self._last_update_time = update.time
                await self.dispatcher.dispatch_raw_update(self, update)

            self._next_offset_id = result.next_offset_id

    def run(
        self,
        function: Optional[
            Union[
                Callable[..., Coroutine[Any, Any, Any]],
                Coroutine[Any, Any, Any]
            ]
        ] = None,
        **kwargs
    ):
        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(self.connect())

            if function is None:
                loop.run_until_complete(self._start_polling())
            elif iscoroutinefunction(function):
                loop.run_until_complete(function(client=self, **kwargs))
            elif iscoroutine(function):
                loop.run_until_complete(function)

        except KeyboardInterrupt:
            pass

        finally:
            if self.dispatcher.is_started:
                loop.run_until_complete(self.shutdown())
            loop.run_until_complete(self.disconnect())

    async def download(self, file_id: str):
        url = await self.get_file(file_id)
        return await self._http_connection.download_file(url)

    async def upload(
        self,
        file: Union[str, Path, bytes],
        file_name: Optional[str] = None,
        file_type: "enums.FileType" = enums.FileType.FILE,
    ):
        url = await self.request_send_file(file_type)
        return await self._http_connection.upload_file(url, file, file_name)
