from dataclasses import dataclass

from .audit_status import AuditStatus
from .delivery_statistics import DeliveryStatistics


@dataclass(frozen=True, slots=True)
class AuditRecord:

    audit_id: 	str
    event_id: 	str
    status: 		AuditStatus
    statistics: DeliveryStatistics
    timestamp: 	str