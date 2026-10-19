from enum import Enum


class TransferStatus(Enum):

    CREATED 	= "created"
    APPROVED 	= "approved"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"