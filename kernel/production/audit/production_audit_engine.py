from .production_audit_entry import ProductionAuditEntry


class ProductionAuditEngine:

    def record(
        self,
        entry: ProductionAuditEntry,
    ) -> ProductionAuditEntry:
        return entry
