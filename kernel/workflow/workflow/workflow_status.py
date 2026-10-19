from enum import Enum


class WorkflowStatus(Enum):

    CREATED 	= "created"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"