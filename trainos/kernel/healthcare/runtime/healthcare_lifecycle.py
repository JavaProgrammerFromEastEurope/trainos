from enum import Enum


class HealthcareLifecycle(Enum):

    CREATED 		= "created"
    INITIALIZED = "initialized"
    RUNNING 		= "running"
    STOPPED 		= "stopped"
    SHUTDOWN 		= "shutdown"