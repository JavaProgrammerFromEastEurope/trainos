from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionAuditEntry:

    audit_id: 	str
    actor_id: 	str
    factory_id: str
    job_id: 		str
    action: 		str