from kernel.simulation.audit.simulation_audit_engine 	import SimulationAuditEngine
from kernel.simulation.audit.simulation_audit_entry 	import SimulationAuditEntry
from kernel.simulation.audit.simulation_audit_type 		import SimulationAuditType


def test_simulation_audit():

    engine = SimulationAuditEngine()
    entry = SimulationAuditEntry(
        audit_id="AUD1",
        tick=100,
        audit_type=SimulationAuditType.TICK_EXECUTED,
        message="Tick completed",
    )
    result = engine.record(entry)
    assert result is entry
