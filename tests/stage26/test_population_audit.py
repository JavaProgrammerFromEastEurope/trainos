from kernel.population.audit.population_audit_engine 	import PopulationAuditEngine
from kernel.population.audit.population_audit_entry 	import PopulationAuditEntry


def test_population_audit():

    engine = PopulationAuditEngine()
    entry = PopulationAuditEntry(
        audit_id="AUD1",
        actor_id="government",
        resident_id="R1",
        action="assign_profession",
    )
    result = engine.record(entry)
    assert result is entry