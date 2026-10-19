from enum import Enum


class AmendmentState(Enum):

    DRAFT 				= "draft"
    SUBMITTED 		= "submitted"
    UNDER_REVIEW 	= "under_review"
    APPROVED 			= "approved"
    RATIFIED 			= "ratified"
    REJECTED 			= "rejected"
    INTEGRATED 		= "integrated"