from kernel.simulation.history.simulation_history_snapshot import (
    SimulationHistorySnapshot,
)

from kernel.simulation.history.simulation_history_entry import SimulationHistoryEntry
from kernel.simulation.history.simulation_history_engine import SimulationHistoryEngine


def test_simulation_history():

    engine = SimulationHistoryEngine()
    snapshot = SimulationHistorySnapshot(
        snapshot_id="HS1",
        tick=500,
        population=9500,
    )
    entry = SimulationHistoryEntry(
        entry_id="HE1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )
    result = engine.record(entry)
    assert result is entry
