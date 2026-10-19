from enum import Enum


class ProductionLifecycle(Enum):

    CREATED 		= "created"
    INITIALIZED = "initialized"
    RUNNING 		= "running"
    STOPPED 		= "stopped"
    SHUTDOWN = "shutdown"