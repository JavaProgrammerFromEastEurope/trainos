from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecurityAuditEntry:

    audit_id: 		str
    actor_id: 		str
    incident_id: 	str
    action: 			str