from enum import Enum


class SecurityIncidentType(Enum):

    UNAUTHORIZED_ACCESS = "unauthorized_access"
    THEFT 							= "theft"
    DISTURBANCE 				= "disturbance"
    EMERGENCY = "emergency"