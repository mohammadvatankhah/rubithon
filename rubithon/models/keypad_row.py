from typing import List

from rubithon import models
from .model import Model


class KeypadRow(Model):

    def __init__(
        self,
        buttons: List["models.Button"],
        **kwargs
    ):
        super().__init__(**kwargs)
        self.buttons = buttons
