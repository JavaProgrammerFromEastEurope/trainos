from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GovernanceAuditEntry:

    audit_id: 		str
    authority_id: str
    decision_id: 	str
    action: 			str