from dataclasses import dataclass, field
from time import time


@dataclass
class ActiveGoalRecord:

    goal_type: str
    sector_id: int | None
    created_at: float = field(default_factory=time)
    cooldown: float = 30.0  # seconds


class ActiveGoalRegistry:

    def __init__(self):
        self.active: dict[str, ActiveGoalRecord] = {}

    def _key(self, goal_type, sector_id):
        return f"{goal_type}:{sector_id}"

    def can_create(self, goal_type, sector_id) -> bool:
        key = self._key(goal_type, sector_id)
        record = self.active.get(key)
        if not record:
            return True
        return (time() - record.created_at) > record.cooldown

    def register(self, goal_type, sector_id):
        key = self._key(goal_type, sector_id)
        self.active[key] = ActiveGoalRecord(
            goal_type=goal_type,
            sector_id=sector_id,
        )

    def clear(self, goal_type, sector_id):
        key = self._key(goal_type, sector_id)
        self.active.pop(key, None)
