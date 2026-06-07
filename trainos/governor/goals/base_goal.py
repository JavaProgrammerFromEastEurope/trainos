from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class GoalState(Enum):

    PENDING 	= "PENDING"
    ACTIVE 		= "ACTIVE"
    COMPLETED = "COMPLETED"
    FAILED 		= "FAILED"


@dataclass(slots=True)
class GovernorGoal:

    priority: int
    state: GoalState = GoalState.PENDING
    goal_id: str = field(
      default_factory=lambda: str(uuid4()))

    def generate_tasks(self):
        raise NotImplementedError
