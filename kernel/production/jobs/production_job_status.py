from enum import Enum


class ProductionJobStatus(Enum):

    CREATED 	= "created"
    VALIDATED = "validated"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"
    CANCELLED = "cancelled"