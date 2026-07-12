from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PolicyConfiguration:

    allow_activation: bool = True
    allow_suspension: bool = True