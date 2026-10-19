from __future__ import annotations

from .goal import Goal
from .goal_state 	import GoalState
from .goal_result import GoalResult


class GoalExecutor:

    def execute(
        self,
        goal: Goal,
    ) -> GoalResult:
        goal.state = GoalState.ACTIVE
        goal.state = GoalState.COMPLETED
        return GoalResult(
            success=True,
        )