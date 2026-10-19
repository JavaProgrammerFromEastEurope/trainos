from enum import Enum


class InstitutionState(Enum):

    CREATED 	= "created"
    ACTIVE 		= "active"
    SUSPENDED = "suspended"
    MERGED 		= "merged"
    DISSOLVED = "dissolved"