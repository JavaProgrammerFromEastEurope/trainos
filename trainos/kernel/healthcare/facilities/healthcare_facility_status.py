from enum import Enum


class HealthcareFacilityStatus(Enum):

    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    CLOSED 			= "closed"