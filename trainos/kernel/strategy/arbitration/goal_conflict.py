from dataclasses import dataclass

from trainos.kernel.strategy.goals.goal import Goal


@dataclass(frozen=True)
class GoalConflict:

    left: 	Goal
    right: 	Goal