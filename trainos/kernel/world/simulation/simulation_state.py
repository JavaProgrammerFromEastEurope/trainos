from enum import Enum


class SimulationState(Enum):

    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED 	= "paused"