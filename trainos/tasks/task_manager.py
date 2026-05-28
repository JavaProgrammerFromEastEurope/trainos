class TaskManager:

    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        return list(self.tasks.values())

    def get_available_tasks(self):
        available = []
        for task in self.tasks.values():
            #
            # TASK FINISHED
            #
            if task.completed:
                continue
            if task.failed:
                continue
            if task.cancelled:
                continue
            #
            # ENOUGH WORKERS
            #
            if task.worker_count >= task.required_workers:
                continue
            available.append(task)
        return available

    def get_active_tasks(self):
        active = []
        for task in self.tasks.values():
            if task.completed:
                continue
            if task.failed:
                continue
            if task.cancelled:
                continue
            if task.worker_count <= 0:
                continue
            active.append(task)
        return active

    def assign_task(self, task_id, entity_id):
        task = self.tasks.get(task_id)
        if not task:
            return False
        if task.completed:
            return False
        if task.failed:
            return False
        if task.cancelled:
            return False
        if task.worker_count >= task.required_workers:
            return False
        if entity_id in task.assigned_entities:
            return False
        task.assign(entity_id)
        return True

    def unassign_task(self, task_id, entity_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.unassign(entity_id)

    def complete_task(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.mark_completed()

    def fail_task(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.mark_failed()

    def cancel_task(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.cancel()

    def reset_task(self, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.reset()

    def advance_task(self, task_id, amount=1.0):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.advance(amount)

    def debug_summary(self):
        summary = []
        for task in self.tasks.values():
            summary.append(
                {
                    "task_id": task.task_id,
                    "workers": (task.worker_count),
                    "required": (task.required_workers),
                    "progress": (task.progress),
                    "completed": (task.completed),
                }
            )
        return summary
