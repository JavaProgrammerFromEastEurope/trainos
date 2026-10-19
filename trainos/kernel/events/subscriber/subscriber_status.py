from enum import Enum


class SubscriberStatus(Enum):

    ACTIVE = "active"
    PAUSED = "paused"
    STOPPED = "stopped"