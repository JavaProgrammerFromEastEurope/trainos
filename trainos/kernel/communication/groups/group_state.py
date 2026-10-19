from enum import Enum


class GroupState(Enum):

    STABLE 		= "stable"
    CONFLICT 	= "conflict"
    RESOLVING = "resolving"