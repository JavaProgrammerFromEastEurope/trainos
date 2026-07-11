from .education_audit_entry import EducationAuditEntry


class EducationAuditEngine:

    def record(
        self,
        entry: EducationAuditEntry,
    ) -> EducationAuditEntry:
        return entry
