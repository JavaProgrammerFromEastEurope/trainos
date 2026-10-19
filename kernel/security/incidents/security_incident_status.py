from enum import Enum


class SecurityIncidentStatus(Enum):

    REPORTED 		= "reported"
    IN_PROGRESS = "in_progress"
    RESOLVED 		= "resolved"
    CLOSED 			= "closed"