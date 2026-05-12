from typing import Optional

from .model import Model


class File(Model):
    attribute_names = [
        ("id", "file_id"),
        ("name", "file_name")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.size = size
