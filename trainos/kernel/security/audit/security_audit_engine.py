from .security_audit_entry import SecurityAuditEntry


class SecurityAuditEngine:

    def record(
        self,
        entry: SecurityAuditEntry,
    ) -> SecurityAuditEntry:
        return entry
