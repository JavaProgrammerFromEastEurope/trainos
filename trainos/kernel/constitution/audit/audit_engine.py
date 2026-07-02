from .constitutional_audit import ConstitutionalAudit


class AuditEngine:

    def record(
        self,
        audit: ConstitutionalAudit,
    ) -> ConstitutionalAudit:
        return audit
