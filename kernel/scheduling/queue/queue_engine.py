from .scheduler_queue import SchedulerQueue

from .queue_status import QueueStatus


class QueueEngine:

    def push(
        self,
        queue: SchedulerQueue,
        task,
    ) -> SchedulerQueue:
        queue.tasks.append(task)
        queue.status = QueueStatus.READY
        return queue

    def pop(self, queue: SchedulerQueue):
        if not queue.tasks:
            queue.status = QueueStatus.EMPTY
            return None
        task = queue.tasks.pop(0)
        if not queue.tasks:
            queue.status = QueueStatus.EMPTY
        return task
