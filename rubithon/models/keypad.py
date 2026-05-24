from copy import deepcopy
from typing import List, Optional

from rubithon import models
from .keypad_row import KeypadRow
from .list import List as RubithonList
from .model import Model


class Keypad(Model):
    attribute_names = [
        ("resize", "resize_keyboard"),
        ("one_time", "one_time_keyboard")
    ]

    def __init__(
        self,
        *rows: List["models.Button"],
        resize: Optional[bool] = None,
        one_time: Optional[bool] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.rows = RubithonList(KeypadRow(row) for row in rows)
        self.resize = resize
        self.one_time = one_time

    @classmethod
    def expected_types(cls):
        base = super().expected_types()
        base["rows"] = List["models.KeypadRow"]
        return base

    @classmethod
    def wrap(cls, raw_model):
        return super().wrap(raw_model)

    def add_button(
        self,
        button: "models.Button",
        row_index: int = -1,
        button_index: int = -1
    ):
        if button_index == -1:
            self.rows[row_index].buttons.append(button)
        elif button_index < 0:
            self.rows[row_index].buttons.insert(button_index + 1, button)
        else:
            self.rows[row_index].buttons.insert(button_index, button)

    def add_row(
        self,
        *rows: "models.Button",
        row_index: int = -1
    ):
        new_row = KeypadRow([])

        if row_index == -1:
            self.rows.append(new_row)
        elif row_index < 0:
            self.rows.insert(row_index + 1, new_row)
        else:
            self.rows.insert(row_index, new_row)

        for button in rows:
            self.add_button(button, row_index)

    def format(self, *args, **kwargs):
        keypad = deepcopy(self)
        for row in keypad.rows:
            for i, button in enumerate(row.buttons):
                row.buttons[i] = button.format(*args, **kwargs)
        return keypad
