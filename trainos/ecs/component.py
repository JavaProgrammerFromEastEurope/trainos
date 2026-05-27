from dataclasses import dataclass, field


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

@dataclass(slots=True)
class SpatialComponent:

    wagon_id: str
    sector_id: str
    cell_x: int = 0
    cell_y: int = 0

@dataclass(slots=True)
class NavigationComponent:

    target_x: int = 0
    target_y: int = 0
    path: list = field(default_factory=list)
    current_index: int = 0
    dirty: bool = True

@dataclass(slots=True)
class TaskComponent:
    current_task_id: str | None = None

@dataclass(slots=True)
class BatteryComponent:
    current_energy: float = 100.0
    max_energy: float = 100.0
    passive_drain: float = 0.02
    movement_drain: float = 0.15
    charging: bool = False
    critical_threshold: float = 15.0

@dataclass(slots=True)
class ChargingStationComponent:
    station_id: str
    occupied: bool = False
    charging_entity: int | None = None