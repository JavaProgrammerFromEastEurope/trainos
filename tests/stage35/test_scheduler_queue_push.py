from kernel.scheduling.queue.scheduler_queue import SchedulerQueue

from kernel.scheduling.queue.queue_engine 	import QueueEngine
from kernel.scheduling.tasks.scheduler_task import SchedulerTask
from kernel.scheduling.tasks.task_priority 	import TaskPriority
from kernel.scheduling.queue.queue_status 	import QueueStatus


def test_scheduler_queue_push():

    queue = SchedulerQueue()
    task = SchedulerTask(
        task_id="TASK-003",
        name="Population Update",
        priority=TaskPriority.NORMAL,
    )

    QueueEngine().push(queue, task)

    assert len(queue.tasks) == 1
    assert queue.status == QueueStatus.READY
