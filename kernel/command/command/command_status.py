from enum import Enum


class CommandStatus(Enum):

    CREATED = "created"
    ACCEPTED = "accepted"
    EXECUTED = "executed"
    FAILED = "failed"
