from __future__ import annotations

from .goap_goal import (
    GOAPGoal,
)

from .goap_plan import (
    GOAPPlan,
)


class GOAPPlanner:

    def plan(
        self,
        goal: GOAPGoal,
    ) -> GOAPPlan:
        return GOAPPlan(actions=[])
