from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionRegistryPolicy:

    unique_identifiers: bool
    allow_replacement: 	bool