from dataclasses import dataclass

from .goal_id import GoalId
from .goal_priority import GoalPriority


@dataclass(frozen=True)
class Goal:

    id: GoalId
    description: str
    priority: GoalPriority