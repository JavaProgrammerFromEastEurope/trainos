from kernel.scheduling.queue.scheduler_queue import SchedulerQueue

from kernel.scheduling.queue.queue_engine 	import QueueEngine
from kernel.scheduling.tasks.scheduler_task import SchedulerTask
from kernel.scheduling.tasks.task_priority 	import TaskPriority


def test_scheduler_queue_pop():

    queue = SchedulerQueue()
    task = SchedulerTask(
        task_id="TASK-004",
        name="Security Patrol",
        priority=TaskPriority.CRITICAL,
    )

    engine = QueueEngine()
    engine.push(queue, task)

    result = engine.pop(queue)
    assert result.task_id == "TASK-004"
    assert len(queue.tasks) == 0
