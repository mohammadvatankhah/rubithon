from typing import Optional

from .model import Model


class AuxData(Model):

    def __init__(
        self,
        start_id: Optional[str] = None,
        button_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.start_id = start_id
        self.button_id = button_id
