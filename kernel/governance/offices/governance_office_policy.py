from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GovernanceOfficePolicy:

    allow_operation: bool = True
    allow_shutdown: bool 	= True