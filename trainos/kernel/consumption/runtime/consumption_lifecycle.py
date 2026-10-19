from enum import Enum


class ConsumptionLifecycle(Enum):

    CREATED 		= "created"
    INITIALIZED = "initialized"
    RUNNING 		= "running"
    STOPPED 		= "stopped"
    SHUTDOWN 		= "shutdown"