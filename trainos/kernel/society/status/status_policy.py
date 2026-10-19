from dataclasses import dataclass


@dataclass(frozen=True)
class StatusPolicy:

    allow_multiple_statuses: 	bool
    immutable_assignment: 		bool