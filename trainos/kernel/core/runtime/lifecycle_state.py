from enum import Enum


class LifecycleState(Enum):

    CREATED 	= "created"
    INITIALIZED = "initialized"
    RUNNING 	= "running"
    STOPPED 	= "stopped"
    SHUTDOWN 	= "shutdown"