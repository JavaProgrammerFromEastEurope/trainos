from dataclasses import dataclass
from .audit_event import AuditEvent


@dataclass(frozen=True)
class BaseAuditEntry:

    entry_id: 	str
    event: 			AuditEvent
    timestamp: 	str