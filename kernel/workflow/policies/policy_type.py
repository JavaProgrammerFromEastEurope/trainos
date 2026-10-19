from enum import Enum


class PolicyType(Enum):

    FAIL_FAST 				= "fail_fast"
    CONTINUE_ON_ERROR = "continue_on_error"
    RETRY 	= "retry"
    STRICT 	= "strict"