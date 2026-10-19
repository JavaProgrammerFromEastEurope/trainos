from enum import Enum


class HandlerStatus(Enum):

    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
