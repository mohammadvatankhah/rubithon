from typing import Optional

from .model import Model


class User(Model):
    attribute_names = [
        ("id", "user_id")
    ]

    def __init__(
        self,
        id: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        phone: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return ""
