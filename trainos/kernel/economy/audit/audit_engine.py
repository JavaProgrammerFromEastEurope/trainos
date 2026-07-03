from .economic_audit_entry import EconomicAuditEntry


class AuditEngine:

    def append(
        self,
        entry: EconomicAuditEntry,
    ) -> EconomicAuditEntry:
        return entry
