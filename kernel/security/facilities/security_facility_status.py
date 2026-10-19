from enum import Enum


class SecurityFacilityStatus(Enum):

    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    CLOSED = "closed"