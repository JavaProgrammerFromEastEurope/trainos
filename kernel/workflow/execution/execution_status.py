from enum import Enum


class ExecutionStatus(Enum):

    CREATED 	= "created"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"