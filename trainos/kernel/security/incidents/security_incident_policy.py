from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityIncidentPolicy:

    allow_resolution: bool 	= True
    allow_closure: bool 		= True