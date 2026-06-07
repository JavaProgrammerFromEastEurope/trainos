from dataclasses import dataclass


@dataclass(slots=True)
class SectorAtmosphere:
    sector_id: int
    oxygen: float
    pressure: float
    co2: float
    population: int
    generator_output: float
    sealed: bool


@dataclass(slots=True)
class AtmosphereSnapshot:
    sectors: dict[int, SectorAtmosphere]
    average_oxygen: float
    minimum_oxygen: float
    average_pressure: float
    reserve_hours: float
    total_population: int


class AtmosphereMonitor:

    def __init__(self, world):
        self.world = world

    def collect(self) -> AtmosphereSnapshot:
        sectors = {}
        oxygen_sum = 0.0
        pressure_sum = 0.0
        total_population = 0
        minimum_oxygen = 100.0

        for sector_id, sector in self.world.sectors.items():
            state = SectorAtmosphere(
                sector_id=sector_id,
                oxygen=sector.oxygen,
                pressure=sector.pressure,
                co2=sector.co2,
                population=sector.population,
                generator_output=sector.generator_output,
                sealed=sector.sealed,
            )
            sectors[sector_id] = state
            oxygen_sum += state.oxygen
            pressure_sum += state.pressure
            total_population += state.population
            minimum_oxygen = min(
                minimum_oxygen,
                state.oxygen,
            )
        count = max(len(sectors), 1)
        return AtmosphereSnapshot(
            sectors=sectors,
            average_oxygen=oxygen_sum / count,
            minimum_oxygen=minimum_oxygen,
            average_pressure=pressure_sum / count,
            reserve_hours=self._estimate_reserve_hours(),
            total_population=total_population,
        )

    def _estimate_reserve_hours(self) -> float:
        oxygen_storage = self.world.resources.oxygen
        consumption = max(
            self.world.statistics.oxygen_consumption_per_hour,
            0.001,
        )
        return oxygen_storage / consumption
