from dataclasses import dataclass
from .base_goal import GovernorGoal


@dataclass(slots=True)
class EvacuateSectorGoal(GovernorGoal):

    source_sector: int
    target_sectors: list[int]
    population: int

    def generate_tasks(self):
        tasks = []
        tasks.append(
            {
                "type": "OPEN_EVACUATION_ROUTE",
                "sector_id": self.source_sector,
            }
        )
        tasks.append(
            {
                "type": "ALLOCATE_TRANSPORT",
                "sector_id": self.source_sector,
            }
        )
        for target in self.target_sectors:
            tasks.append(
                {
                    "type": "RESERVE_BEDS",
                    "sector_id": target,
                }
            )
        tasks.append(
            {
                "type": "MOVE_POPULATION",
                "count": self.population,
                "source": self.source_sector,
            }
        )
        return tasks
