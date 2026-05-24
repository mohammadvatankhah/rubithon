from typing import Optional

from rubithon import enums, models
from .model import Model


class ButtonLocation(Model):
    attribute_names = [
        ("default_pointer", "default_pointer_location"),
        ("default_map", "default_map_location")
    ]

    def __init__(
        self,
        title: str,
        type: Optional["enums.ButtonLocationType"] = enums.ButtonLocationType.PICKER,
        default_pointer: Optional["models.Location"] = None,
        default_map: Optional["models.Location"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.type = type
        self.default_pointer_location = default_pointer
        self.default_map_location = default_map
