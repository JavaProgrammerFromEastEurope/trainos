from dataclasses import dataclass, field

from trainos.ecs.roles import DroneRole


@dataclass(slots=True)
class PositionComponent:

    x: float = 0.0
    y: float = 0.0


@dataclass(slots=True)
class VelocityComponent:

    dx: float = 0.0
    dy: float = 0.0


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

    #
    # TARGET (SET ONCE)
    #
    target_x: int | None = None
    target_y: int | None = None
    #
    # PATH (COMPUTED ONCE)
    #
    path: list[tuple[int, int]] = field(default_factory=list)
    #
    # STATE FLAGS
    #
    dirty: bool 				= False
    blocked_ticks: int 	= 0
    destination_reached: bool = False
    #
    # INTERNAL CONTROL
    #
    last_target: tuple[int, int] | None = None


@dataclass(slots=True)
class TaskComponent:
    current_task_id: str | None = None
    executing_task: bool = False
    cooperative: bool = False


@dataclass(slots=True)
class BatteryComponent:
    #
    # CURRENT ENERGY
    #
    level: float = 100.0
    #
    # MAX ENERGY
    #
    max_level: float = 100.0
    #
    # ENERGY LOSS PER TICK
    #
    consumption_rate: float = 0.05
    #
    # CHARGING STATE
    #
    charging: bool = False
    #
    # LOW ENERGY THRESHOLD
    #
    critical_threshold: float = 20.0
    #
    # AI STATE
    #
    seeking_charge: bool = False


@dataclass(slots=True)
class ChargingStationComponent:
    station_id: str
    occupied: bool = False
    charging_entity: int | None = None
    reserved_by: int | None = None


@dataclass(slots=True)
class RoleComponent:
    role: DroneRole = DroneRole.GENERAL
    efficiency: float = 1.0
