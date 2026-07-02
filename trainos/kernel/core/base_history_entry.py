from dataclasses import dataclass


@dataclass(frozen=True)
class BaseHistoryEntry:

    entity_id: 		str
    version: 			str
    description: 	str