import asyncio
from asyncio import Queue
from os import cpu_count
from typing import List, Optional

import rubithon
from rubithon import dispatcher, models

from .chain import Chain
from ..event_handlers import EventHandler


def is_subclass(cls: type, super_cls: type):
    if not isinstance(cls, type):
        return False
    return issubclass(cls, super_cls)


class Dispatcher:
    reasonable_async_workers = min(32, (cpu_count() or 1) + 4) * 5

    def __init__(
        self,
        client: "rubithon.Client",
        async_workers: Optional[int] = None
    ):
        self.client = client
        self.async_workers = async_workers or self.reasonable_async_workers

        self.is_started = False
        self.queue = Queue()
        self.workers: List["asyncio.Task"] = []

    async def start(self):
        if self.is_started:
            return

        self.is_started = True

        for _ in range(self.async_workers):
            task = asyncio.create_task(self._worker())
            self.workers.append(task)

    async def stop(self):
        if not self.is_started:
            return

        self.is_started = False

        for _ in self.workers:
            await self.queue.put(None)

        for worker in self.workers:
            await worker

        self.workers.clear()

    async def dispatch_event(
        self,
        client: "rubithon.Client",
        event
    ):
        await self.queue.put((client, event))

    async def dispatch_raw_update(
        self,
        client: "rubithon.Client",
        update: "models.Update"
    ):
        effective = update.get_effective_update()
        effective.bind(client)
        await self.queue.put((client, effective))

    async def _worker(self):
        while self.is_started or not self.queue.empty():
            item = await self.queue.get()

            if item is None:
                break

            client, event = item
            await self._propagate_chain(client, client, event)

    async def _propagate_chain(
        self,
        chain: "dispatcher.Chain",
        client: "rubithon.Client",
        event
    ):
        for child in chain.children:
            if isinstance(child, Chain):
                await self._propagate_chain(child, client, event)
                break

            if isinstance(child, EventHandler):
                if isinstance(event, child.can_handle) or is_subclass(event, child.can_handle):
                    try:
                        await child.handle(client=client, event=event)
                    except Exception as error:
                        await self.dispatch_event(client, error)
                    break

        for sub_chain in chain.chains:
            await self._propagate_chain(sub_chain, client, event)
