from enum import Enum


class FaultType(Enum):

    MINOR 		= "minor"
    MAJOR 		= "major"
    CRITICAL 	= "critical"