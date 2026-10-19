from enum import Enum


class StepStatus(Enum):

    CREATED 	= "created"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"