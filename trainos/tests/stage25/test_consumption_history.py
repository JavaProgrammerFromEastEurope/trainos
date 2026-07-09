from kernel.consumption.history.consumption_history_engine import ConsumptionHistoryEngine
from kernel.consumption.history.consumption_history_entry import ConsumptionHistoryEntry
from kernel.consumption.history.consumption_snapshot import ConsumptionSnapshot

from kernel.consumption.jobs.consumption_job_status import ConsumptionJobStatus


def test_consumption_history():

    engine = ConsumptionHistoryEngine()

    snapshot = ConsumptionSnapshot(
        snapshot_id="SNAP1",
        job_id="JOB1",
        status=ConsumptionJobStatus.COMPLETED,
    )
    entry = ConsumptionHistoryEntry(
        entry_id="ENTRY1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)
    assert result is entry