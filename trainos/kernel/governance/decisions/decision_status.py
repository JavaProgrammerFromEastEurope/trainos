from enum import Enum


class DecisionStatus(Enum):

    PROPOSED = "proposed"
    APPROVED = "approved"
    EXECUTED = "executed"
    REJECTED = "rejected"