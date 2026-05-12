from inspect import iscoroutinefunction
from typing import Callable

from ..smart_call import remove_unwanted_parameters


class EventHandler:
    can_handle = object

    def __init__(self, callback: Callable):
        self.callback = callback
        self.self = None

    def to_string(self, keyword="if", tabs=0):
        result = []
        condition = self.condition or self.can_handle.__name__
        result.append(f"{keyword} {condition}:")
        result.append(f"    {type(self).__name__}({self.can_handle.__name__})")
        return "\n".join(f"{'    ' * tabs}{i}" for i in result)

    def __repr__(self):
        return self.to_string()

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        client = kwargs["client"]

        if self.self is not None:
            args = list(args)
            args.insert(0, self.self)

        if event is not None:
            kwargs["event"] = event

        args, kwargs = remove_unwanted_parameters(self.callback, *args, **kwargs)

        if iscoroutinefunction(self.callback):
            return await self.callback(*args, **kwargs)
        return self.callback(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        args, kwargs = remove_unwanted_parameters(self.callback, *args, **kwargs)
        return self.callback(*args, **kwargs)
