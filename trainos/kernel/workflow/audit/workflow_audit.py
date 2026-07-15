from dataclasses import dataclass

from .audit_status import AuditStatus
from .audit_statistics import AuditStatistics


@dataclass(frozen=True, slots=True)
class WorkflowAudit:

    audit_id: 		str
    workflow_id: 	str
    status: 		AuditStatus
    statistics: AuditStatistics
    timestamp: 		str