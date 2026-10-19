from enum import Enum


class DeliveryJobStatus(Enum):

    CREATED 	= "created"
    READY 		= "ready"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"
    CANCELLED = "cancelled"