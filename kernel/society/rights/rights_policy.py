from dataclasses import dataclass


@dataclass(frozen=True)
class RightsPolicy:

    allow_duplicate_rights: bool
    immutable_assignment: 	bool