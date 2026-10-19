from enum import Enum


class TreatmentStatus(Enum):

    PLANNED 	= "planned"
    ACTIVE 		= "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"