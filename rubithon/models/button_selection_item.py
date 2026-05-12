from typing import Optional

from .model import Model


class ButtonSelectionItem(Model):

    def __init__(
        self,
        text: Optional[str] = None,
        image_url: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.image_url = image_url
        self.type = type
