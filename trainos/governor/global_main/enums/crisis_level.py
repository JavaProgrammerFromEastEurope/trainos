from enum import IntEnum


class CrisisLevel(IntEnum):

    NORMAL 		= 0
    WARNING 	= 1
    SERIOUS 	= 2
    CRITICAL 	= 3
    EXTINCTION = 4