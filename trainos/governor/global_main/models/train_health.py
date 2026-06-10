from dataclasses import dataclass


@dataclass(slots=True)
class TrainHealth:

    value: float
    oxygen_score: float
    power_score: float
    reactor_score: float
    food_score: float
    water_score: float
