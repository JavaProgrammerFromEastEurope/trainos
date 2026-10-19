from .audit_record import AuditRecord


class AuditEngine:

    def record(
        self,
        record: AuditRecord,
    ) -> AuditRecord:
        return record
