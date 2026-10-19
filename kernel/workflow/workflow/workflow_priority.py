from enum import IntEnum


class WorkflowPriority(IntEnum):

    LOW = 10
    NORMAL = 50
    HIGH = 100
    CRITICAL = 1000