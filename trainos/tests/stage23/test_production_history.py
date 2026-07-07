from kernel.production.history.production_history_engine import ProductionHistoryEngine
from kernel.production.history.production_history_entry import ProductionHistoryEntry
from kernel.production.history.production_snapshot import ProductionSnapshot

from kernel.production.jobs.production_job_status import ProductionJobStatus


def test_production_history():

    engine = ProductionHistoryEngine()

    snapshot = ProductionSnapshot(
        snapshot_id="SNAP1",
        job_id="JOB1",
        status=ProductionJobStatus.COMPLETED,
    )

    entry = ProductionHistoryEntry(
        entry_id="ENTRY1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)

    assert result is entry
