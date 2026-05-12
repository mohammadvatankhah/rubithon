from typing import Optional

from .model import Model


class ContactMessage(Model):

    def __init__(
        self,
        phone_number: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
