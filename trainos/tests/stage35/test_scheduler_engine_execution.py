from kernel.scheduling.engine.scheduler_engine import SchedulerEngine

from kernel.scheduling.queue.scheduler_queue import SchedulerQueue
from kernel.scheduling.tasks.scheduler_task import SchedulerTask
from kernel.scheduling.tasks.task_priority import TaskPriority


def test_scheduler_engine_execution():

    queue = SchedulerQueue()
    task = SchedulerTask(
        task_id="TASK-005",
        name="Persistence Snapshot",
        priority=TaskPriority.LOW,
    )

    queue.tasks.append(task)
    result = SchedulerEngine().execute_next(queue)
    assert result.success is True
    assert result.task_id == "TASK-005"
