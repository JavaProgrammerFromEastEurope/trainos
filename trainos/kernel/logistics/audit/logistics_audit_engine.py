from .logistics_audit_entry import LogisticsAuditEntry


class LogisticsAuditEngine:

    def record(
        self,
        entry: LogisticsAuditEntry,
    ) -> LogisticsAuditEntry:
        return entry