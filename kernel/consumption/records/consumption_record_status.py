from enum import Enum


class ConsumptionRecordStatus(Enum):

    RECORDED = "recorded"
    VERIFIED = "verified"
    REJECTED = "rejected"