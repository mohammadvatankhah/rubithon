from typing import Optional

from rubithon import enums, models

from .model import Model


class Button(Model):
    attribute_names = [
        ("text", "button_text"),
        ("selection", "button_selection"),
        ("calendar", "button_calendar"),
        ("number_picker", "button_number_picker"),
        ("string_picker", "button_string_picker"),
        ("location", "button_location"),
        ("textbox", "button_textbox")
    ]

    def __init__(
        self,
        id: str,
        text: str,
        type: "enums.ButtonType" = enums.ButtonType.SIMPLE,
        selection: Optional["models.ButtonSelection"] = None,
        calendar: Optional["models.ButtonCalendar"] = None,
        number_picker: Optional["models.ButtonNumberPicker"] = None,
        string_picker: Optional["models.ButtonStringPicker"] = None,
        location: Optional["models.ButtonLocation"] = None,
        textbox: Optional["models.ButtonTextbox"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.text = text
        self.type = type
        self.selection = selection
        self.calendar = calendar
        self.number_picker = number_picker
        self.string_picker = string_picker
        self.location = location
        self.textbox = textbox
