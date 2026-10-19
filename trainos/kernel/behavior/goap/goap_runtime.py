from __future__ import annotations

from .goap_planner import (
    GOAPPlanner,
)


class GOAPRuntime:

    def __init__(
        self,
    ) -> None:
        self.planner = GOAPPlanner()
