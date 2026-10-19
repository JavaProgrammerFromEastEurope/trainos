from dataclasses import dataclass

from .goal_type import GoalType


@dataclass
class Goal:

    type: GoalType
