from dataclasses import dataclass


@dataclass(frozen=True)
class CivilHistoryEntry:

    entity_id: 		str
    version: 			str
    description: 	str