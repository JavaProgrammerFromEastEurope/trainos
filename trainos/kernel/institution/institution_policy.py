from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionPolicy:

    require_unique_identifier: bool
    require_type: bool