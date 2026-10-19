from enum import Enum


class TimerStatus(Enum):

    CREATED = "created"
    RUNNING = "running"
    PAUSED 	= "paused"
    STOPPED = "stopped"