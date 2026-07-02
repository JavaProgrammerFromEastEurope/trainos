from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionHistoryPolicy:

    immutable_history: 		bool
    chronological_order: 	bool