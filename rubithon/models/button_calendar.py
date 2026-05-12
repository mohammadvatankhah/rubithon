from typing import Optional

from rubithon import enums

from .model import Model


class ButtonCalendar(Model):

    def __init__(
        self,
        title: str,
        type: "enums.ButtonCalendarType" = enums.ButtonCalendarType.DATETIME,
        min_year: Optional[str] = None,
        max_year: Optional[str] = None,
        default_value: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.type = type
        self.min_year = min_year
        self.max_year = max_year
        self.default_value = default_value
