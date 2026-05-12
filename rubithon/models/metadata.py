from typing import List, Optional

from rubithon import models

from .model import Model


class Metadata(Model):

    def __init__(
        self,
        parts: Optional[List["models.MetadataPart"]] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.parts = parts
