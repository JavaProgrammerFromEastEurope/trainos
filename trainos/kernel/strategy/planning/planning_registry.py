from __future__ import annotations

from .strategic_plan import StrategicPlan


class PlanningRegistry:

    def __init__(self) -> None:
        self._plans: list[StrategicPlan] = []

    def register(self, plan: StrategicPlan) -> None:
        self._plans.append(plan)

    def plans(self) -> tuple[StrategicPlan, ...]:
        return tuple(self._plans)
