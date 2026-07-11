from enum import Enum


class EducationLifecycle(Enum):

    CREATED 			= "created"
    INITIALIZED 	= "initialized"
    RUNNING 			= "running"
    STOPPED 			= "stopped"
    SHUTDOWN 			= "shutdown"