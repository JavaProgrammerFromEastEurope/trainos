from kernel.simulation.snapshot.simulation_snapshot_engine import (
    SimulationSnapshotEngine,
)

from kernel.simulation.snapshot.simulation_snapshot import SimulationSnapshot
from kernel.simulation.snapshot.clock_snapshot import ClockSnapshot
from kernel.simulation.snapshot.runtime_snapshot import RuntimeSnapshot
from kernel.simulation.snapshot.scheduler_snapshot import SchedulerSnapshot
from kernel.simulation.snapshot.event_snapshot import EventSnapshot
from kernel.simulation.clock.clock_status import ClockStatus
from kernel.simulation.runtime.runtime_status import RuntimeStatus
from kernel.simulation.scheduler.scheduler_status import SchedulerStatus


def test_simulation_snapshot():

    engine = SimulationSnapshotEngine()
    snapshot = SimulationSnapshot(
        snapshot_id="SNAP1",
        clock=ClockSnapshot(
            clock_id="CLOCK1",
            tick=1000,
            status=ClockStatus.RUNNING,
        ),
        runtime=RuntimeSnapshot(
            runtime_id="RUNTIME1",
            status=RuntimeStatus.RUNNING,
        ),
        scheduler=SchedulerSnapshot(
            scheduler_id="SCH1",
            status=SchedulerStatus.RUNNING,
        ),
        events=(
            EventSnapshot(
                event_id="EVENT1",
                tick=1000,
            ),
        ),
    )
    result = engine.capture(snapshot)
    assert result is snapshot
