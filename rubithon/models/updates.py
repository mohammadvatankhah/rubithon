from typing import List, Optional

from rubithon import models

from .model import Model


class Updates(Model):

    def __init__(
        self,
        updates: Optional[List["models.Update"]] = None,
        next_offset_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.updates = updates
        self.next_offset_id = next_offset_id
