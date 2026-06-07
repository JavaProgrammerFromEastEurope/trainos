from dataclasses import dataclass

from .base_goal import GovernorGoal


@dataclass(slots=True)
class ContainLeakGoal(GovernorGoal):

    sector_id: int
    leak_rate: float

    def generate_tasks(self):
        return [
            {
                "type": "CLOSE_BULKHEAD",
                "sector_id": self.sector_id,
            },
            {
                "type": "DISPATCH_ENGINEERS",
                "sector_id": self.sector_id,
            },
            {
                "type": "REPAIR_HULL",
                "sector_id": self.sector_id,
            },
            {
                "type": "REPRESSURIZE",
                "sector_id": self.sector_id,
            },
        ]
