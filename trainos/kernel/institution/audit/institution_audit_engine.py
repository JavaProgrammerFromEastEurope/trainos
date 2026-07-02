from .institution_audit_entry import InstitutionAuditEntry


class InstitutionAuditEngine:

    def record(
        self,
        entry: InstitutionAuditEntry,
    ) -> InstitutionAuditEntry:
        return entry