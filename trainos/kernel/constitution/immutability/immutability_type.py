from enum import Enum


class ImmutabilityType(Enum):

    ABSOLUTE 			= "absolute"
    SUPERMAJORITY = "supermajority"
    AMENDABLE = "amendable"