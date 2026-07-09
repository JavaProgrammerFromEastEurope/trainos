from enum import Enum


class ConsumptionJobStatus(Enum):

    CREATED		= "created"
    READY 		= "ready"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"
    CANCELLED = "cancelled"