from typing import Optional

from rubithon import enums

from .model import Model


class ButtonTextbox(Model):

    def __init__(
        self,
        title: str,
        type_line: "enums.ButtonTextboxTypeLine" = enums.ButtonTextboxTypeLine.MULTILINE,
        type_keypad: Optional["enums.ButtonTextboxTypeKeypad"] = enums.ButtonTextboxTypeKeypad.STRING,
        place_holder: Optional[str] = None,
        default_value: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.type_line = type_line
        self.type_keypad = type_keypad
        self.place_holder = place_holder
        self.default_value = default_value
