from enum import Enum


class GoalState(Enum):

    PENDING 	= "pending"
    ACTIVE 		= "active"
    COMPLETED = "completed"
    FAILED 		= "failed"
    CANCELLED = "cancelled"