from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityFacilityPolicy:

    allow_operation: bool = True
    allow_shutdown: bool 	= True