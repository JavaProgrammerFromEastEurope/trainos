from .simulation_audit_entry import SimulationAuditEntry


class SimulationAuditEngine:

    def record(
        self,
        entry: SimulationAuditEntry,
    ) -> SimulationAuditEntry:
        return entry
