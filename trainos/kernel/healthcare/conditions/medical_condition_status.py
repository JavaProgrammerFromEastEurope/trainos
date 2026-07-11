from enum import Enum


class MedicalConditionStatus(Enum):

    ACTIVE 		= "active"
    IMPROVING = "improving"
    RESOLVED 	= "resolved"
    CHRONIC 	= "chronic"