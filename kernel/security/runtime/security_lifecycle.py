from enum import Enum


class SecurityLifecycle(Enum):

    CREATED 		= "created"
    INITIALIZED = "initialized"
    RUNNING 		= "running"
    STOPPED 		= "stopped"
    SHUTDOWN 		= "shutdown"