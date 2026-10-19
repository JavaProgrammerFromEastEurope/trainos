from enum import Enum


class ClockStatus(Enum):

    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED 	= "paused"