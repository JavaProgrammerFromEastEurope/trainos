from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionPolicy:

    allow_creation: 	bool
    allow_retirement: bool