class Task:

    def __init__(
        self,
        task_id,
        task_type,
        target_wagon,
        target_sector,
        target_x,
        target_y,
        priority=1,
        duration=120,
        required_workers=1,
        required_role=None,
    ):

        # identity
        self.task_id 		= task_id
        self.task_type 	= task_type
        # world target
        self.target_wagon 	= target_wagon
        self.target_sector 	= target_sector
        self.target_x = target_x
        self.target_y = target_y
        # execution
        self.priority = priority
        self.duration = duration
        self.progress = 0
        # worker requirements
        self.required_workers = required_workers
        self.required_role = required_role
        # ownership
        self.assigned_entities = set()
        # lifecycle
        self.started 		= False
        self.completed 	= False
        self.failed 		= False
        self.cancelled 	= False
        self.finished 	= False

    @property
    def worker_count(self):
        return len(self.assigned_entities)

    @property
    def has_required_workers(self):
        return self.worker_count >= self.required_workers

    @property
    def progress_percent(self):
        if self.duration <= 0:
            return 100.0
        return round((self.progress / self.duration) * 100, 2)

    @property
    def is_available(self):
        return (
            not self.completed
            and not self.failed
            and not self.cancelled
            and self.worker_count < self.required_workers
        )

    @property
    def is_active(self):
        return self.worker_count > 0 and not self.completed

    def assign(self, entity_id):
        self.assigned_entities.add(entity_id)

    def unassign(self, entity_id):
        if entity_id in self.assigned_entities:
            self.assigned_entities.remove(entity_id)

    def mark_started(self):
        self.started 		= True

    def mark_completed(self):
        self.completed 	= True
        self.finished 	= True

    def mark_failed(self):
        self.failed 		= True
        self.finished 	= True

    def cancel(self):
        self.cancelled 	= True
        self.finished 	= True

    def advance(self, amount=1.0):
        if self.completed:
            return
        if self.failed:
            return
        if self.cancelled:
            return
        self.progress += amount
        if self.progress >= self.duration:
            self.progress = self.duration
            self.mark_completed()

    def reset(self):
        self.progress 	= 0
        self.started 		= False
        self.completed 	= False
        self.failed 		= False
        self.cancelled 	= False
        self.finished 	= False
        self.assigned_entities.clear()

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "target_wagon": self.target_wagon,
            "target_sector": self.target_sector,
            "target_x": self.target_x,
            "target_y": self.target_y,
            "priority": self.priority,
            "duration": self.duration,
            "progress": self.progress,
            "required_workers": self.required_workers,
            "required_role": (self.required_role.value if self.required_role else None),
            "assigned_entities": list(self.assigned_entities),
            "started": self.started,
            "completed": self.completed,
            "failed": self.failed,
            "cancelled": self.cancelled,
            "finished": self.finished,
        }

    def __repr__(self):
        return (
            f"Task("
            f"id={self.task_id}, "
            f"type={self.task_type}, "
            f"workers="
            f"{self.worker_count}/"
            f"{self.required_workers}, "
            f"progress="
            f"{self.progress}/"
            f"{self.duration}, "
            f"completed="
            f"{self.completed}"
            f")"
        )
