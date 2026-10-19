from enum import Enum


class TaskStatus(Enum):

    SUCCESS = "success"
    FAILURE = "failure"
    RUNNING = "running"
    IDLE 		= "idle"
