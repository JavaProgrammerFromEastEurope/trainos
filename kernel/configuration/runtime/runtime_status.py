from enum import Enum


class ConfigurationRuntimeStatus(Enum):

    CREATED = "created"
    RUNNING = "running"
    PAUSED 	= "paused"
    STOPPED = "stopped"