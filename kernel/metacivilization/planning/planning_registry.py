from __future__ import annotations

from .long_term_plan import LongTermPlan


class PlanningRegistry:

    def __init__(self) -> None:
        self._plans: list[LongTermPlan] = []

    def add(self, plan: LongTermPlan) -> None:
        self._plans.append(plan)

    def plans(self) -> tuple[LongTermPlan, ...]:
        return tuple(self._plans)
