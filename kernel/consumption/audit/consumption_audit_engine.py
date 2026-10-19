from .consumption_audit_entry import ConsumptionAuditEntry


class ConsumptionAuditEngine:

    def record(
        self,
        entry: ConsumptionAuditEntry,
    ) -> ConsumptionAuditEntry:
        return entry