from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionHistoryEntry:

    institution_id: str
    version: 				str
    description: 		str