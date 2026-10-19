from __future__ import annotations

from .goap_plan import (
    GOAPPlan,
)


class GOAPHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[GOAPPlan] = []

    def add(
        self,
        plan: GOAPPlan,
    ) -> None:
        self._history.append(plan)

    def records(
        self,
    ) -> tuple[GOAPPlan, ...]:
        return tuple(self._history)
