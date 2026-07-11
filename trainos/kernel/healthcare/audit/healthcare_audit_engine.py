from .healthcare_audit_entry import HealthcareAuditEntry


class HealthcareAuditEngine:

    def record(
        self,
        entry: HealthcareAuditEntry,
    ) -> HealthcareAuditEntry:
        return entry
