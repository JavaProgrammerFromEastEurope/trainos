from enum import Enum


class ValidationResult(Enum):

    VALID 	= "valid"
    INVALID = "invalid"
    REQUIRES_REVIEW = "requires_review"