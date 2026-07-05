from .resource_audit_entry import ResourceAuditEntry


class ResourceAuditEngine:

    def record(
        self,
        entry: ResourceAuditEntry,
    ) -> ResourceAuditEntry:
        return entry
