from .goal import Goal
from .goal_type import GoalType


class GoalEngine:

    def determine(self) -> Goal:
        return Goal(type=GoalType.SURVIVAL)
