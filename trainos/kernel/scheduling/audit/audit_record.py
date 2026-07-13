from dataclasses import dataclass

from .audit_status import AuditStatus
from .execution_statistics import ExecutionStatistics


@dataclass(frozen=True, slots=True)
class AuditRecord:

    audit_id: 	str
    task_id: 		str
    status: 		AuditStatus
    statistics: ExecutionStatistics
    timestamp: 	str