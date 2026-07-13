from kernel.scheduling.tasks.scheduler_task import SchedulerTask

from kernel.scheduling.tasks.task_priority import TaskPriority
from kernel.scheduling.tasks.task_engine import TaskEngine
from kernel.scheduling.tasks.task_status import TaskStatus


def test_task_lifecycle():

    task = SchedulerTask(
        task_id="TASK-002",
        name="Healthcare Scan",
        priority=TaskPriority.NORMAL,
    )

    engine = TaskEngine()
    task = engine.ready(task)
    assert task.status == TaskStatus.READY

    task = engine.start(task)
    assert task.status == TaskStatus.RUNNING

    task = engine.complete(task)
    assert task.status == TaskStatus.COMPLETED
