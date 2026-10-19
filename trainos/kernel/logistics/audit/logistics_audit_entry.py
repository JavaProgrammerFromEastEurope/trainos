from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LogisticsAuditEntry:

    audit_id: 		str
    actor_id: 		str
    job_id: 			str
    shipment_id: 	str
    action: str