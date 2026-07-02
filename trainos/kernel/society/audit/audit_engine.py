from .civil_audit_entry import CivilAuditEntry


class AuditEngine:

    def append(
        self,
        entry: CivilAuditEntry,
    ) -> CivilAuditEntry:
        return entry
