from __future__ import annotations

from .htn_planner import (
    HTNPlanner,
)


class HTNRuntime:

    def __init__(
        self,
    ) -> None:
        self.planner = HTNPlanner()
