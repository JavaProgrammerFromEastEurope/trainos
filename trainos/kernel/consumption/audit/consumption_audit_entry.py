from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionAuditEntry:

    audit_id: 		str
    actor_id: 		str
    consumer_id: 	str
    job_id: 			str
    action: 			str