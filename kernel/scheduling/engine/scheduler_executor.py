from kernel.scheduling.tasks.scheduler_task import SchedulerTask

from .execution_result import ExecutionResult


class SchedulerExecutor:

    def execute(
        self,
        task: SchedulerTask,
    ) -> ExecutionResult:
        return ExecutionResult(
            success=True,
            task_id=task.task_id,
        )
