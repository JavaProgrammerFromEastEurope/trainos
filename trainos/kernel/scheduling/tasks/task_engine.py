from .scheduler_task import SchedulerTask

from .task_status import TaskStatus


class TaskEngine:

    def ready(
        self,
        task: SchedulerTask,
    ) -> SchedulerTask:
        return SchedulerTask(
            task_id=task.task_id,
            name=task.name,
            priority=task.priority,
            status=TaskStatus.READY,
        )

    def start(
        self,
        task: SchedulerTask,
    ) -> SchedulerTask:
        return SchedulerTask(
            task_id=task.task_id,
            name=task.name,
            priority=task.priority,
            status=TaskStatus.RUNNING,
        )

    def complete(
        self,
        task: SchedulerTask,
    ) -> SchedulerTask:
        return SchedulerTask(
            task_id=task.task_id,
            name=task.name,
            priority=task.priority,
            status=TaskStatus.COMPLETED,
        )
