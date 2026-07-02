from dataclasses import dataclass


@dataclass(frozen=True)
class CivilAuditEntry:

    entity_id: 	str
    action: 		str
    actor: 			str
    reason: 		str