from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionPolicy:

    allow_amendment: bool
    require_supermajority: bool