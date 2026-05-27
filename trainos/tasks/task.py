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
    ):

        # unique task identifier
        self.task_id = task_id
        # repair / mining / hauling / etc
        self.task_type = task_type
        # world location
        self.target_wagon = target_wagon
        self.target_sector = target_sector
        self.target_x = target_x
        self.target_y = target_y
        # utility importance
        self.priority = priority
        # execution duration in ticks
        self.duration = duration
        # current execution progress
        self.progress = 0
        # lifecycle flags
        self.completed = False
        self.failed = False
        self.cancelled = False
        # entity ownership
        self.assigned_entity = None
        # execution state
        self.started = False
        self.finished = False

        self.required_workers = required_workers
        self.assigned_entities = set()

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
            and self.assigned_entity is None
        )

    @property
    def worker_count(self):
        return len(self.assigned_entities)

    @property
    def has_required_workers(self):
        return self.worker_count >= self.required_workers

    def assign(self, entity_id):
        self.assigned_entities.add(entity_id)

    def unassign(self, entity_id):
        if entity_id in self.assigned_entities:
            self.assigned_entities.remove(entity_id)

    @property
    def is_active(self):
        return self.assigned_entity is not None and not self.completed

    def assign(self, entity_id):
        self.assigned_entity = entity_id

    def unassign(self):
        self.assigned_entity = None

    def mark_started(self):
        self.started = True

    def mark_completed(self):
        self.completed = True
        self.finished = True

    def mark_failed(self):
        self.failed = True
        self.finished = True

    def cancel(self):
        self.cancelled = True
        self.finished = True

    def advance(self, amount=1):
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
        self.progress = 0
        self.completed = False
        self.failed = False
        self.cancelled = False
        self.started = False
        self.finished = False
        self.assigned_entity = None

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
            "completed": self.completed,
            "failed": self.failed,
            "cancelled": self.cancelled,
            "assigned_entity": self.assigned_entity,
            "started": self.started,
            "finished": self.finished,
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            task_id=data["task_id"],
            task_type=data["task_type"],
            target_wagon=data["target_wagon"],
            target_sector=data["target_sector"],
            target_x=data["target_x"],
            target_y=data["target_y"],
            priority=data.get("priority", 1),
            duration=data.get("duration", 120),
        )
        task.progress = data.get("progress", 0)
        task.completed = data.get("completed", False)
        task.failed = data.get("failed", False)
        task.cancelled = data.get("cancelled", False)
        task.assigned_entity = data.get("assigned_entity")
        task.started = data.get("started", False)
        task.finished = data.get("finished", False)
        return task

    def __repr__(self):

        return (
            f"Task("
            f"id={self.task_id}, "
            f"type={self.task_type}, "
            f"target=("
            f"{self.target_x}, "
            f"{self.target_y}"
            f"), "
            f"priority={self.priority}, "
            f"progress="
            f"{self.progress}/"
            f"{self.duration}, "
            f"completed="
            f"{self.completed}"
            f")"
        )
