from enum import Enum


class AuditStatus(Enum):

    STARTED 	= "started"
    COMPLETED = "completed"
    FAILED 		= "failed"