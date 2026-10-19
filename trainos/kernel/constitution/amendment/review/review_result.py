from enum import Enum


class ReviewResult(Enum):

    PENDING 	= "pending"
    ACCEPTED 	= "accepted"
    REJECTED 	= "rejected"
    REVISION_REQUIRED = "revision_required"