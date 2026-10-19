from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionAuditEntry:

    institution_id: str
    action: 				str
    actor: 					str
    reason: 				str