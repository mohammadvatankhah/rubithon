from typing import Optional

from rubithon import enums
from .model import Model


class MetadataPart(Model):

    def __init__(
        self,
        type: Optional["enums.MetadataPartType"] = None,
        from_index: Optional[int] = None,
        length: Optional[int] = None,
        link_url: Optional[str] = None,
        mention_text_user_id: Optional[str] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.type = type
        self.from_index = from_index
        self.length = length
        self.link_url = link_url
        self.mention_text_user_id = mention_text_user_id
