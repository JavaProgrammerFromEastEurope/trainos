from dataclasses import dataclass


@dataclass(slots=True)
class PressureState:

    sector_id: int
    pressure: float
    inflow: 	float
    outflow: 	float
    delta: 		float

class PressureModel:
    def __init__(self, world):
        self.world = world

    def evaluate(self) -> dict[int, PressureState]:
        states = {}
        for sector_id, sector in self.world.sectors.items():
            inflow = sector.air_inflow
            outflow = sector.air_outflow
            delta = inflow - outflow
            states[sector_id] = PressureState(
                sector_id=sector_id,
                pressure=sector.pressure,
                inflow=inflow,
                outflow=outflow,
                delta=delta,
            )
        return states