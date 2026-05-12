from ..event_handlers import (
    ConnectHandler,
    DisconnectHandler,
    ErrorHandler,
    EventHandler,
    InitializeHandler,
    MessageHandler,
    RemovedMessageHandler,
    ShutdownHandler,
    StartedBotHandler,
    StoppedBotHandler,
    UpdateHandler,
    UpdatedMessageHandler
)


class Chain:

    def __init__(self, name, *chains):
        self.name = name
        self.chains = list(chains)

        self.children = []
        for attribute_name in dir(self):
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, EventHandler):
                attribute.self = self
                self.add_event_handler(attribute)

    @staticmethod
    def create_event_handler(event_handler, *args, **kwargs):
        def decorator(callback):
            return event_handler(callback, *args, **kwargs)
        return decorator

    def add_event_handler(self, event_handler, *args, **kwargs):
        if isinstance(event_handler, type):
            def decorator(callback):
                event_handler_instance = event_handler(callback, *args, **kwargs)
                self.add_event_handler(event_handler_instance)
                return event_handler_instance
            return decorator
        self.children.append(event_handler)

    @classmethod
    def connect_handler(cls):
        return cls.create_event_handler(ConnectHandler)

    def on_connect(self):
        return self.add_event_handler(ConnectHandler)

    @classmethod
    def initialize_handler(cls):
        return cls.create_event_handler(InitializeHandler)

    def on_initialize(self):
        return self.add_event_handler(InitializeHandler)

    @classmethod
    def event_handler(cls):
        return cls.create_event_handler(EventHandler)

    def on_event(self):
        return self.add_event_handler(EventHandler)

    @classmethod
    def error_handler(cls):
        return cls.create_event_handler(ErrorHandler)

    def on_error(self):
        return self.add_event_handler(ErrorHandler)

    @classmethod
    def update_handler(cls):
        return cls.create_event_handler(UpdateHandler)

    def on_update(self):
        return self.add_event_handler(UpdateHandler)

    @classmethod
    def message_handler(cls):
        return cls.create_event_handler(MessageHandler)

    def on_message(self):
        return self.add_event_handler(MessageHandler)

    @classmethod
    def removed_message_handler(cls):
        return cls.create_event_handler(RemovedMessageHandler)

    def on_removed_message(self):
        return self.add_event_handler(RemovedMessageHandler)

    @classmethod
    def started_bot_handler(cls):
        return cls.create_event_handler(StartedBotHandler)

    def on_started_bot(self):
        return self.add_event_handler(StartedBotHandler)

    @classmethod
    def stopped_bot_handler(cls):
        return cls.create_event_handler(StoppedBotHandler)

    def on_stopped_bot(self):
        return self.add_event_handler(StoppedBotHandler)

    @classmethod
    def updated_message_handler(cls):
        return cls.create_event_handler(UpdatedMessageHandler)

    def on_updated_message(self):
        return self.add_event_handler(UpdatedMessageHandler)

    @classmethod
    def shutdown_handler(cls):
        return cls.create_event_handler(ShutdownHandler)

    def on_shutdown(self):
        return self.add_event_handler(ShutdownHandler)

    @classmethod
    def disconnect_handler(cls):
        return cls.create_event_handler(DisconnectHandler)

    def on_disconnect(self):
        return self.add_event_handler(DisconnectHandler)

    def remove_event_handler(self, event_handler):
        self.children.remove(event_handler)

    def add(self, *chains):
        self.children.extend(chains)

    def include(self, *chains):
        self.chains.extend(chains)

    def get(self, name):
        for chain in self.chains:
            if chain.name == name:
                return chain
        raise ValueError(f"Chain \"{name}\" does not exist")

    def delete(self, name):
        for i, c in enumerate(self.chains):
            if c.name == name:
                del self.chains[i]
                return
        for i, c in enumerate(self.children):
            if isinstance(c, Chain) and c.name == name:
                del self.children[i]
                return
        raise ValueError(f"Chain \"{name}\" does not exist")
