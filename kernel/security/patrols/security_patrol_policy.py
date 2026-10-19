from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityPatrolPolicy:

    allow_activation: bool = True
    allow_completion: bool = True