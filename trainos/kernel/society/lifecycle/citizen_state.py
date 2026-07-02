from enum import Enum


class CitizenState(Enum):

    BORN 			= "born"
    ACTIVE 		= "active"
    SUSPENDED = "suspended"
    MIGRATED 	= "migrated"
    DECEASED 	= "deceased"