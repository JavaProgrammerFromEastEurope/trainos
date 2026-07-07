from kernel.logistics.history.logistics_history_engine import LogisticsHistoryEngine
from kernel.logistics.history.logistics_history_entry import LogisticsHistoryEntry
from kernel.logistics.history.logistics_snapshot import LogisticsSnapshot

from kernel.logistics.jobs.delivery_job_status import DeliveryJobStatus


def test_logistics_history():

    engine = LogisticsHistoryEngine()

    snapshot = LogisticsSnapshot(
        snapshot_id="SNAP1",
        job_id="JOB1",
        status=DeliveryJobStatus.COMPLETED,
    )

    entry = LogisticsHistoryEntry(
        entry_id="ENTRY1",
        timestamp="2026-01-01T00:00:00Z",
        snapshot=snapshot,
    )

    result = engine.record(entry)

    assert result is entry
