from typing import Optional

from rubithon import models

from .model import Model


class Sticker(Model):
    attribute_names = [
        ("id", "sticker_id")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        file: Optional["models.File"] = None,
        emoji_character: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.file = file
        self.emoji_character = emoji_character
