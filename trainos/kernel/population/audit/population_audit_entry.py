from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PopulationAuditEntry:

    audit_id: 		str
    actor_id: 		str
    resident_id: 	str
    action: 			str