class TaskAllocator:

    def allocate(self, task, entities):
        assigned = []
        for e in entities:
            if not e.available:
                continue
            if not self._can_do(e, task):
                continue
            assigned.append(e.entity_id)
            if len(assigned) >= task.get("required", 1):
                break
        return assigned

    def _can_do(self, entity, task):
        if task["type"] == "CONTAIN":
            return entity.role in ["ENGINEER", "MAINTENANCE"]
        if task["type"] == "MOVE_POPULATION":
            return entity.role in ["HAULER"]
        return True

