from enum import Enum


class RollbackResult(Enum):

    SUCCESS 	= "success"
    FAILED 		= "failed"
    FORBIDDEN = "forbidden"