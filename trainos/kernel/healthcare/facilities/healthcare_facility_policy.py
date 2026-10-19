from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HealthcareFacilityPolicy:

    allow_treatment: bool = True
    allow_shutdown: bool 	= True