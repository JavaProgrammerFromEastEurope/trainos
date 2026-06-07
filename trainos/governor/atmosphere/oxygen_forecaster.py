from dataclasses import dataclass

@dataclass(slots=True)
class OxygenForecast:
    sector_id: int
    oxygen_10m: float
    oxygen_1h: float
    time_to_critical: float

class OxygenForecaster:
    CRITICAL_LEVEL = 70.0

    def __init__(self, world):
        self.world = world

    def forecast(self) -> dict[int, OxygenForecast]:
        result = {}
        for sector_id, sector in self.world.sectors.items():
            rate 				= sector.oxygen_change_rate
            oxygen_10m 	= sector.oxygen + rate * 10
            oxygen_1h 	= sector.oxygen + rate * 60
            if rate >= 0:
                hours = float("inf")
            else:
                hours = (
                    sector.oxygen
                    - self.CRITICAL_LEVEL
                ) / abs(rate)
            result[sector_id] = OxygenForecast(
                sector_id=sector_id,
                oxygen_10m=oxygen_10m,
                oxygen_1h=oxygen_1h,
                time_to_critical=hours,
            )
        return result