from .governance_audit_entry import GovernanceAuditEntry


class GovernanceAuditEngine:

    def record(
        self,
        entry: GovernanceAuditEntry,
    ) -> GovernanceAuditEntry:
        return entry
