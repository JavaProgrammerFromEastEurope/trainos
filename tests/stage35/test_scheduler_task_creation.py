from kernel.scheduling.tasks.scheduler_task import SchedulerTask

from kernel.scheduling.tasks.task_priority 	import TaskPriority
from kernel.scheduling.tasks.task_status 		import TaskStatus


def test_scheduler_task_creation():
    task = SchedulerTask(
        task_id="TASK-001",
        name="Simulation Tick",
        priority=TaskPriority.HIGH,
    )
    assert task.task_id == "TASK-001"
    assert task.name == "Simulation Tick"
    assert task.priority == TaskPriority.HIGH
    assert task.status == TaskStatus.CREATED
