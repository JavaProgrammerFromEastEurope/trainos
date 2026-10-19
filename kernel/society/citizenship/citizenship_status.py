from enum import Enum


class CitizenshipStatus(Enum):

    NONE 			= "none"
    APPLIED 	= "applied"
    GRANTED 	= "granted"
    SUSPENDED = "suspended"
    REVOKED 	= "revoked"