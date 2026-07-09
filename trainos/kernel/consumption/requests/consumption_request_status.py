from enum import Enum


class ConsumptionRequestStatus(Enum):

    CREATED 	= "created"
    APPROVED 	= "approved"
    REJECTED 	= "rejected"
    FULFILLED = "fulfilled"
    CANCELLED = "cancelled"