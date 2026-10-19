from enum import Enum


class SchedulerStatus(Enum):

    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED 	= "paused"