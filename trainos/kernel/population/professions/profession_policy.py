from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProfessionPolicy:

    allow_assignment: bool = True
    require_training: bool = False