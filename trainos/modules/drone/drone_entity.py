from dataclasses import dataclass


@dataclass(slots=True)
class DroneEntity:

    drone_id: str
    x: float = 0.0
    y: float = 0.0
    battery: float = 100.0
    active: bool = True
