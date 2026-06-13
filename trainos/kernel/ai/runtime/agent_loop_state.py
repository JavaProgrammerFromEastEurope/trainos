from enum import Enum


class AgentLoopState(Enum):

    STOPPED 	= "stopped"
    RUNNING 	= "running"
    PAUSED 		= "paused"