from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HealthcareAuditEntry:

    audit_id: 	str
    actor_id: 	str
    patient_id: str
    action: 		str