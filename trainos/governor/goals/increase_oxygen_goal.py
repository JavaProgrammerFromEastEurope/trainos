from dataclasses 	import dataclass
from .base_goal 	import GovernorGoal


@dataclass(slots=True)
class IncreaseOxygenGoal(GovernorGoal):

    sector_id: int
    deficit: float
    def generate_tasks(self):
        return [
            {
                "type": "START_GENERATOR",
                "sector_id": self.sector_id,
            },
            {
                "type": "CLEAN_FILTER",
                "sector_id": self.sector_id,
            },
            {
                "type": "BOOST_COMPRESSOR",
                "sector_id": self.sector_id,
            },
        ]