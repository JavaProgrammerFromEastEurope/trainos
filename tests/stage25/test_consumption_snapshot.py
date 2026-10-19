from kernel.consumption.consumers.consumer_status import ConsumerStatus
from kernel.consumption.jobs.consumption_job_status import ConsumptionJobStatus
from kernel.consumption.records.consumption_record_status import ConsumptionRecordStatus
from kernel.consumption.requests.consumption_request_status import ConsumptionRequestStatus
from kernel.consumption.runtime.consumption_lifecycle import ConsumptionLifecycle
from kernel.consumption.snapshot.consumer_snapshot import ConsumerSnapshot
from kernel.consumption.snapshot.consumption_job_snapshot import ConsumptionJobSnapshot
from kernel.consumption.snapshot.consumption_record_snapshot import ConsumptionRecordSnapshot
from kernel.consumption.snapshot.consumption_request_snapshot import ConsumptionRequestSnapshot
from kernel.consumption.snapshot.consumption_runtime_snapshot import ConsumptionRuntimeSnapshot
from kernel.consumption.snapshot.consumption_snapshot import ConsumptionSnapshot
from kernel.consumption.snapshot.consumption_snapshot_engine import ConsumptionSnapshotEngine


def test_consumption_snapshot():

    engine = ConsumptionSnapshotEngine()

    snapshot = ConsumptionSnapshot(
        snapshot_id="SNAP1",
        runtime=ConsumptionRuntimeSnapshot(
            lifecycle=ConsumptionLifecycle.RUNNING,
        ),
        consumers=(
            ConsumerSnapshot(
                consumer_id="C1",
                status=ConsumerStatus.ACTIVE,
            ),
        ),
        requests=(
            ConsumptionRequestSnapshot(
                request_id="REQ1",
                status=ConsumptionRequestStatus.APPROVED,
            ),
        ),
        jobs=(
            ConsumptionJobSnapshot(
                job_id="JOB1",
                status=ConsumptionJobStatus.RUNNING,
            ),
        ),
        records=(
            ConsumptionRecordSnapshot(
                record_id="REC1",
                status=ConsumptionRecordStatus.VERIFIED,
            ),
        ),
    )

    result = engine.capture(snapshot)
    assert result is snapshot