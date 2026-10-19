from kernel.production.factories.factory_status import FactoryStatus
from kernel.production.jobs.production_job_status import ProductionJobStatus

from kernel.production.runtime.production_lifecycle import ProductionLifecycle

from kernel.production.snapshot.production_factory_snapshot import (
    ProductionFactorySnapshot,
)
from kernel.production.snapshot.production_job_snapshot import (
    ProductionJobSnapshot,
)
from kernel.production.snapshot.production_runtime_snapshot import (
    ProductionRuntimeSnapshot,
)
from kernel.production.snapshot.production_snapshot import ProductionSnapshot
from kernel.production.snapshot.production_snapshot_engine import (
    ProductionSnapshotEngine,
)


def test_production_snapshot():

    engine = ProductionSnapshotEngine()
    snapshot = ProductionSnapshot(
        snapshot_id="SNAP1",
        runtime=ProductionRuntimeSnapshot(
            lifecycle=ProductionLifecycle.RUNNING,
        ),
        factories=(
            ProductionFactorySnapshot(
                factory_id="factory1",
                status=FactoryStatus.ACTIVE,
            ),
        ),
        jobs=(
            ProductionJobSnapshot(
                job_id="job1",
                status=ProductionJobStatus.RUNNING,
            ),
        ),
    )

    result = engine.capture(snapshot)
    assert result is snapshot
