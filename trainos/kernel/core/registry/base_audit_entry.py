from dataclasses import dataclass


@dataclass(frozen=True)
class BaseAuditEntry:

    entity_id: 	str
    action: 		str
    actor: 			str
    reason: 		str