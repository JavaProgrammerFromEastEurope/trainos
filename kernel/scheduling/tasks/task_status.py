from enum import Enum


class TaskStatus(Enum):

    CREATED 	= "created"
    READY 		= "ready"
    RUNNING 	= "running"
    COMPLETED = "completed"
    FAILED 		= "failed"