from enum import Enum


class DelegationScope(Enum):

    TEMPORARY = "temporary"
    PERMANENT = "permanent"
    EMERGENCY = "emergency"