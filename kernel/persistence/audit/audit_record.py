from dataclasses import dataclass

from .audit_operation import AuditOperation
from .audit_status import AuditStatus


@dataclass(frozen=True, slots=True)
class AuditRecord:

    audit_id: 	str
    object_id: 	str
    operation: 	AuditOperation
    status: 		AuditStatus
    timestamp: 	str