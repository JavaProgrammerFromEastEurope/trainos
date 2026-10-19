from dataclasses import dataclass


@dataclass(frozen=True)
class DutiesPolicy:

    immutable_assignment: 	bool
    allow_duplicate_duties: bool