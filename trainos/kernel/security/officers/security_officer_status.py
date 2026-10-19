from enum import Enum


class SecurityOfficerStatus(Enum):

    AVAILABLE 	= "available"
    ON_DUTY 		= "on_duty"
    RESPONDING 	= "responding"
    OFF_DUTY 		= "off_duty"