from __future__ import annotations

from .htn_plan import HTNPlan
from .htn_task import HTNTask


class HTNPlanner:

    def plan(
        self,
        task: HTNTask,
    ) -> HTNPlan:
        return HTNPlan(tasks=[task])
