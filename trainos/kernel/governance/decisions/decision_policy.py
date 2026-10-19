from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DecisionPolicy:

    allow_execution: bool = True
    allow_rejection: bool = True