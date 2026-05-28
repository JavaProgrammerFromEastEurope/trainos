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
        required_workers=1,
        required_role=None,
        interaction_radius=1,
        duration=500,
    ):
        #
        # IDENTIFICATION
        #
        self.task_id = task_id
        self.task_type = task_type
        #
        # TARGET LOCATION
        #
        self.target_wagon = target_wagon
        self.target_sector = target_sector
        self.target_x = target_x
        self.target_y = target_y
        #
        # PRIORITY
        #
        self.priority = priority
        #
        # COOPERATIVE EXECUTION
        #
        self.required_workers = required_workers
        self.required_role = required_role
        #
        # NEW:
        # interaction distance
        #
        self.interaction_radius = interaction_radius
        #
        # TASK STATE
        #
        self.assigned_entities = []
        self.started 		= False
        self.completed 	= False
        self.failed 		= False
        self.cancelled 	= False
        #
        # EXECUTION
        #
        self.progress = 0
        self.duration = duration
        #
        # compatibility
        #
        self.required_progress = duration

    @property
    def progress_percent(self):
        if self.duration <= 0:
            return 100
        return round((self.progress / self.duration) * 100, 2)

    def assign_entity(self, entity_id):
        if entity_id not in (self.assigned_entities):
            self.assigned_entities.append(entity_id)

    def unassign_entity(self, entity_id):
        if entity_id in (self.assigned_entities):
            self.assigned_entities.remove(entity_id)

    def mark_started(self):
        self.started = True

    def mark_completed(self):
        self.completed = True

    def mark_failed(self):
        self.failed = True

    def cancel(self):
        self.cancelled = True

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
