from typing import Optional

from rubithon import models
from .model import Model


class Bot(Model):
    attribute_names = [
        ("id", "bot_id"),
        ("title", "bot_title")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        title: Optional[str] = None,
        avatar: Optional["models.File"] = None,
        description: Optional[str] = None,
        username: Optional[str] = None,
        start_message: Optional[str] = None,
        share_url: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.title = title
        self.avatar = avatar
        self.description = description
        self.username = username
        self.start_message = start_message
        self.share_url = share_url
