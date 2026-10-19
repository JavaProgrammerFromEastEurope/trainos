from enum import Enum


class PopulationLifecycle(Enum):

    CREATED 		= "created"
    INITIALIZED = "initialized"
    RUNNING 		= "running"
    STOPPED 		= "stopped"
    SHUTDOWN 		= "shutdown"