from typing import List, Optional

from rubithon import models
from .model import Model


class Poll(Model):
    attribute_names = [
        ("status", "poll_status")
    ]

    def __init__(
        self,
        question: Optional[str] = None,
        options: Optional[List[str]] = None,
        status: Optional["models.PollStatus"] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.question = question
        self.options = options
        self.status = status
