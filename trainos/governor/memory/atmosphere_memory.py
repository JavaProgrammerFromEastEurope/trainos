from dataclasses import dataclass, field


@dataclass
class SectorMemory:

    oxygen_trend: float = 0.0
    last_oxygen: float 	= 100.0
    instability_score: float = 0.0
    leak_history: int = 0


class AtmosphereMemory:

    def __init__(self):
        self.sectors: dict[int, SectorMemory] = {}

    def get(self, sector_id: int) -> SectorMemory:
        if sector_id not in self.sectors:
            self.sectors[sector_id] = SectorMemory()
        return self.sectors[sector_id]

    def update_oxygen(self, sector_id: int, oxygen: float):
        mem = self.get(sector_id)
        mem.oxygen_trend = oxygen - mem.last_oxygen
        mem.last_oxygen = oxygen
        if oxygen < 80:
            mem.instability_score += 0.1
        else:
            mem.instability_score *= 0.95
