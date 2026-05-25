from dataclasses import dataclass


@dataclass(slots=True)
class PositionComponent:

    x: float = 0.0
    y: float = 0.0


@dataclass(slots=True)
class VelocityComponent:

    dx: float = 0.0
    dy: float = 0.0


@dataclass(slots=True)
class BatteryComponent:

    level: float = 100.0

    consumption_rate: float = 0.5


@dataclass(slots=True)
class DroneComponent:

    drone_id: str


@dataclass(slots=True)
class StatusComponent:

    active: bool = True
