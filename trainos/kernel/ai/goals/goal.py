from __future__ import annotations

from dataclasses import dataclass
from .goal_priority import GoalPriority
from .goal_state 		import GoalState


@dataclass
class Goal:
  
    id: str
    description: str
    priority: GoalPriority 	= GoalPriority.NORMAL
    state: GoalState 				= GoalState.PENDING