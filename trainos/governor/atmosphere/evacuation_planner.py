from dataclasses import dataclass


@dataclass(slots=True)
class EvacuationPlan:
  
    source_sector: int
    target_sectors: list[int]
    population: int


class EvacuationPlanner:

    def __init__(self, world):
        self.world = world

    def build_plan(
        self,
        sector_id: int,
    ) -> EvacuationPlan:
        sector = self.world.sectors[sector_id]
        safe = []

        for candidate in self.world.sectors.values():
            if candidate.sealed:
                continue
            if candidate.oxygen < 90:
                continue
            safe.append(candidate.sector_id)
        return EvacuationPlan(
            source_sector=sector_id,
            target_sectors=safe,
            population=sector.population,
        )
