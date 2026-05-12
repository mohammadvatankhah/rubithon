from typing import Optional, List

from .model import Model


class ButtonStringPicker(Model):

    def __init__(
        self,
        title: str,
        items: Optional[List[str]] = None,
        default_value: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.items = items
        self.default_value = default_value
