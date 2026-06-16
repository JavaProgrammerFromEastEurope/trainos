from trainos.kernel.behavior.tasks.task import (
    Task,
)

from trainos.kernel.behavior.tasks.task_status import TaskStatus


def test_task_graph():

    task = Task()
    result = task.execute()
    assert result.status == TaskStatus.SUCCESS
