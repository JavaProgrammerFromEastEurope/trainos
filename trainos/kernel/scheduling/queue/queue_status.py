from enum import Enum


class QueueStatus(Enum):

    EMPTY = "empty"
    READY = "ready"
    PROCESSING = "processing"