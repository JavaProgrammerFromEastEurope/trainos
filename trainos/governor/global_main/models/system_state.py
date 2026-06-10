from dataclasses import dataclass, field


@dataclass(slots=True)
class SystemState:

    oxygen_global: 		float = 100.0
    power_global: 		float = 100.0
    pressure_global: 	float = 1.
    reactor_health: 	float = 100.0
    population_alive: int = 0
    food_supply_days: int = 365
    water_supply_days: int = 365
    oxygen_per_wagon: 	dict[int, float] = field(default_factory=dict)
    power_per_wagon: 		dict[int, float] = field(default_factory=dict)
    pressure_per_wagon: dict[int, float] = field(default_factory=dict)
    wagon_health: 			dict[int, float] = field(default_factory=dict)
