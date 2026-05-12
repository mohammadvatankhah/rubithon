from typing import Optional

from .model import Model


class Location(Model):

    def __init__(
        self,
        longitude: Optional[str] = None,
        latitude: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.longitude = longitude
        self.latitude = latitude
