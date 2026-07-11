from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityOfficerPolicy:

    allow_dispatch: bool 		= True
    allow_stand_down: bool 	= True