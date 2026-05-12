from enum import Enum
from typing import Any


class NameEnum(Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return  "".join(word.capitalize() for word in name.lower().split("_"))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return super().__eq__(other)
        if isinstance(other, str):
            return self.value == other
        return False
