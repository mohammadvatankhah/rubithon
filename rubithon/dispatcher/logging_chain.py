import logging
from typing import Optional

import rubithon

from .chain import Chain


class LoggingChain(Chain):

    def __init__(
        self,
        name: str = "logging",
        logger: Optional["logging.Logger"] = None
    ):
        super().__init__(name)
        self.log = logger or logging.getLogger(self.name)

    @Chain.error_handler()
    def log_error(self, error: Exception):
        self.log.exception(error)

    @Chain.connect_handler()
    def log_connect(self, client: "rubithon.Client"):
        self.log.info(f"{client} connected")

    @Chain.initialize_handler()
    def log_initialize(self, client: "rubithon.Client"):
        self.log.info(f"{client} initialized (async workers: {client.dispatcher.async_workers})")

    @Chain.shutdown_handler()
    def log_shutdown(self, client: "rubithon.Client"):
        self.log.info(f"{client} shutting down")

    @Chain.disconnect_handler()
    def log_disconnect(self, client: "rubithon.Client"):
        self.log.info(f"{client} disconnected")

    @Chain.event_handler()
    def log_event(self, event):
        self.log.info(event)
