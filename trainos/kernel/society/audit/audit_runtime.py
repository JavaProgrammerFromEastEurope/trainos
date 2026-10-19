from .audit_engine import AuditEngine


class AuditRuntime:

    def __init__(self) -> None:
        self._engine = AuditEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.append(entry)

    def shutdown(self) -> None:
        pass
