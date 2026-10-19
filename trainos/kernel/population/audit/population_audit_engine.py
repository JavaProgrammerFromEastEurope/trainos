from .population_audit_entry import PopulationAuditEntry


class PopulationAuditEngine:

    def record(
        self,
        entry: PopulationAuditEntry,
    ) -> PopulationAuditEntry:
        return entry