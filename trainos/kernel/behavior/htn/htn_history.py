from __future__ import annotations

from .htn_plan import (
    HTNPlan,
)


class HTNHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[HTNPlan] = []

    def add(
        self,
        plan: HTNPlan,
    ) -> None:
        self._history.append(plan)

    def records(
        self,
    ) -> tuple[HTNPlan, ...]:
        return tuple(self._history)
