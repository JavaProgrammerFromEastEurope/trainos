from dataclasses import dataclass


@dataclass(frozen=True)
class CitizenshipPolicy:

    allow_dual_citizenship: bool
    require_approval: 			bool