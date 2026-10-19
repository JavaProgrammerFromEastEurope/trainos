from kernel.scheduling.queue.queue_engine import QueueEngine

from .scheduler_executor import SchedulerExecutor


class SchedulerEngine:

    def __init__(self):
        self.queue = QueueEngine()
        self.executor = SchedulerExecutor()

    def execute_next(
        self,
        scheduler_queue,
    ):
        task = self.queue.pop(scheduler_queue)
        if task is None:
            return None
        return self.executor.execute(task)
