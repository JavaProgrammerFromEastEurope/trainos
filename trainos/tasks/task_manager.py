from trainos.tasks.task import Task


class TaskManager:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def get_available_tasks(self):
        available = []
        for task in self.tasks.values():
            if task.completed:
                continue
            if task.assigned_entity:
                continue
            available.append(task)
        available.sort(key=lambda t: t.priority, reverse=True)
        return available

    def assign_task(self, task_id, entity_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.assigned_entity = entity_id

    def complete_task(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.completed = True
