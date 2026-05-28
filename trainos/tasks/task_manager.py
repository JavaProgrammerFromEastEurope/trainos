class TaskManager:

    def __init__(self):
        #
        # task_id -> Task
        #
        self.tasks = {}

    #
    # REGISTER TASK
    #
    def add_task(self, task):
        self.tasks[task.task_id] = task

    #
    # REMOVE TASK
    #
    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    #
    # GET TASK
    #
    def get_task(self, task_id):
        return self.tasks.get(task_id)

    #
    # AVAILABLE TASKS
    #
    # Returns:
    # tasks that:
    # - are not completed
    # - are not failed
    # - are not cancelled
    # - still need workers
    #
    def get_available_tasks(self):
        available = []
        for task in self.tasks.values():
            #
            # SKIP FINISHED TASKS
            #
            if task.completed:
                continue
            if task.failed:
                continue
            if task.cancelled:
                continue
            #
            # TASK FULL
            #
            if len(task.assigned_entities) >= task.required_workers:
                continue
            available.append(task)
        #
        # SORT BY PRIORITY
        #
        # highest priority first
        #
        available.sort(key=lambda task: task.priority, reverse=True)
        return available

    #
    # ENTITY TASKS
    #
    def get_tasks_for_entity_role(self, role):
        compatible = []
        for task in self.get_available_tasks():
            #
            # NO ROLE REQUIRED
            #
            if task.required_role is None:
                compatible.append(task)
                continue
            #
            # ROLE MATCH
            #
            if task.required_role == role:
                compatible.append(task)
        return compatible

    #
    # ASSIGN ENTITY
    #
    def assign_entity_to_task(self, entity_id, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return False
        #
        # TASK FINISHED
        #
        if task.completed:
            return False
        if task.failed:
            return False
        if task.cancelled:
            return False
        #
        # TASK FULL
        #
        if len(task.assigned_entities) >= task.required_workers:
            return False
        #
        # ALREADY ASSIGNED
        #
        if entity_id in (task.assigned_entities):
            return True
        #
        # ASSIGN
        #
        task.assign_entity(entity_id)
        return True

    #
    # UNASSIGN ENTITY
    #
    def unassign_entity_from_task(self, entity_id, task_id):
        task = self.tasks.get(task_id)
        if not task:
            return
        task.unassign_entity(entity_id)

    #
    # CLEAN FINISHED TASKS
    #
    def cleanup_tasks(self):
        to_remove = []
        for task_id, task in self.tasks.items():
            if task.completed:
                to_remove.append(task_id)
            elif task.failed:
                to_remove.append(task_id)
            elif task.cancelled:
                to_remove.append(task_id)
        for task_id in to_remove:
            del self.tasks[task_id]
