from typing import List, Optional

from rubithon import enums, models

from .model import Model


class ButtonSelection(Model):
    attribute_names = [
        ("id", "selection_id")
    ]

    def __init__(
        self,
        id: str,
        title: str,
        columns_count: str,
        items: List["models.ButtonSelectionItem"],
        search_type: Optional["enums.ButtonSelectionSearchType"] = None,
        get_type: "enums.ButtonSelectionGetType" = enums.ButtonSelectionGetType.LOCAL,
        is_multi_selection: bool = False,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.id = id
        self.title = title
        self.columns_count = columns_count
        self.items = items
        self.search_type = search_type
        self.get_type = get_type
        self.is_multi_selection = is_multi_selection
