from kernel.scheduling.snapshot.scheduler_snapshot import (
    SchedulerSnapshot,
)

from kernel.scheduling.snapshot.queue_snapshot 			import QueueSnapshot
from kernel.scheduling.snapshot.timer_snapshot 			import TimerSnapshot
from kernel.scheduling.snapshot.execution_snapshot 	import ExecutionSnapshot
from kernel.scheduling.snapshot.snapshot_engine 		import SnapshotEngine


def test_scheduler_snapshot():
    snapshot = SchedulerSnapshot(
        snapshot_id="SNAP-001",
        queue=QueueSnapshot(
            queued_tasks=15,
        ),
        timer=TimerSnapshot(
            tick=100,
        ),
        execution=ExecutionSnapshot(
            completed_tasks=500,
        ),
    )
    result = SnapshotEngine().capture(snapshot)
    assert result.snapshot_id == "SNAP-001"
    assert result.queue.queued_tasks == 15
    assert result.timer.tick == 100
    assert result.execution.completed_tasks == 500
