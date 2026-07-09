from enum import Enum


class ConsumptionRequestPriority(Enum):

    LOW 		= "low"
    NORMAL 	= "normal"
    HIGH 		= "high"
    CRITICAL = "critical"