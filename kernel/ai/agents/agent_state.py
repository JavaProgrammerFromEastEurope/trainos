from enum import Enum


class AgentState(Enum):

    IDLE 				= "idle"
    THINKING 		= "thinking"
    EXECUTING 	= "executing"
    WAITING 		= "waiting"
    FAILED 			= "failed"