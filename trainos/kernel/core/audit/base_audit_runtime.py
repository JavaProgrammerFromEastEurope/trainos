from .base_audit_entry import BaseAuditEntry


class BaseAuditRuntime:

    def initialize(self) -> None:
        pass

    def record(self, entry: BaseAuditEntry) -> BaseAuditEntry:
        return entry

    def shutdown(self) -> None:
        pass