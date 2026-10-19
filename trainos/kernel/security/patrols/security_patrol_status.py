from enum import Enum


class SecurityPatrolStatus(Enum):

    PLANNED 	= "planned"
    ACTIVE 		= "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"