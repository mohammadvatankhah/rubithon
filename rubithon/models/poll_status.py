from typing import List, Optional

from rubithon import enums
from .model import Model


class PollStatus(Model):

    def __init__(
        self,
        state: Optional["enums.PollState"] = None,
        selection_index: Optional[int] = None,
        percent_vote_options: Optional[List[int]] = None,
        total_vote: Optional[int] = None,
        show_total_votes: Optional[bool] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.state = state
        self.selection_index = selection_index
        self.percent_vote_options = percent_vote_options
        self.total_vote = total_vote
        self.show_total_votes = show_total_votes
