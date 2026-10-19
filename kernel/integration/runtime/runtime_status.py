from enum import Enum


class IntegrationRuntimeStatus(Enum):

    CREATED = "created"
    RUNNING = "running"
    PAUSED 	= "paused"
    STOPPED = "stopped"