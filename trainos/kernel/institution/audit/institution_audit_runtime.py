from .institution_audit_engine import InstitutionAuditEngine


class InstitutionAuditRuntime:

    def __init__(self) -> None:
        self._engine = InstitutionAuditEngine()

    def initialize(self) -> None:
        pass

    def update(self, entry):
        return self._engine.record(entry)

    def shutdown(self) -> None:
        pass
