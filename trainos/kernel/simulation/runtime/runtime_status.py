from enum import Enum


class RuntimeStatus(Enum):

    CREATED 	= "created"
    RUNNING 	= "running"
    PAUSED 		= "paused"
    STOPPED 	= "stopped"