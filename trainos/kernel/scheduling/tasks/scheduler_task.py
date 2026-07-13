from dataclasses import dataclass

from .task_priority import TaskPriority
from .task_status 	import TaskStatus


@dataclass(frozen=True, slots=True)
class SchedulerTask:

    task_id: 	str
    name: 		str
    priority: TaskPriority
    status: TaskStatus = TaskStatus.CREATED