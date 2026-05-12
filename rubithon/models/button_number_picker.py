from typing import Optional

from .model import Model


class ButtonNumberPicker(Model):

    def __init__(
        self,
        title: str,
        min_value: Optional[str] = None,
        max_value: Optional[str] = None,
        default_value: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.min_value = min_value
        self.max_value = max_value
        self.default_value = default_value
