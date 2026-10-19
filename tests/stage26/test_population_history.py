from kernel.population.history.population_history_engine import PopulationHistoryEngine
from kernel.population.history.population_history_entry import PopulationHistoryEntry
from kernel.population.history.population_snapshot import PopulationSnapshot
from kernel.population.residents.resident_status import ResidentStatus


def test_population_history():

    engine = PopulationHistoryEngine()
    snapshot = PopulationSnapshot(
        snapshot_id="SNAP1",
        resident_id="R1",
        status=ResidentStatus.ACTIVE,
    )
    entry = PopulationHistoryEntry(
        entry_id="ENTRY1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )
    result = engine.record(entry)
    assert result is entry