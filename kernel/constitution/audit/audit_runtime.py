from .audit_engine import AuditEngine


class AuditRuntime:

    def __init__(self) -> None:
        self._engine = AuditEngine()

    def initialize(self) -> None:
        pass

    def update(self, audit):
        return self._engine.record(audit)

    def shutdown(self) -> None:
        pass
