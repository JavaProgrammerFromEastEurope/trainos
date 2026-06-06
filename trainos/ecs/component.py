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


from dataclasses import dataclass


@dataclass(slots=True)
class DroneComponent:
    #
    # UNIQUE DRONE ID
    #
    drone_id: str
    #
    # DRONE ROLE
    # ENGINEER / MINER / HAULER / SCOUT
    #
    role: str = "WORKER"
    #
    # DRONE CLASSIFICATION
    #
    drone_type: str = "GROUND"
    #
    # ENTITY ACTIVE FLAG
    #
    enabled: bool = True
    #
    # CURRENT STATE
    #
    state: str = "IDLE"
    #
    # CURRENT PRIORITY
    #
    priority: int = 0
    #
    # AI FLAGS
    #
    autonomous: bool = True
    cooperative: bool = False
    #
    # MOVEMENT PROFILE
    #
    max_speed: float = 1.0
    acceleration: float = 1.0
    #
    # OPERATIONAL LIMITS
    #
    interaction_range: int = 1
    sensor_range: int = 6
    #
    # CURRENT ASSIGNED TASK
    #
    assigned_task: str | None = None
    #
    # CURRENT TARGET ENTITY
    #
    target_entity: int | None = None
    #
    # FAILURE FLAGS
    #
    damaged: bool = False
    stuck: bool = False
    offline: bool = False
    #
    # INTERNAL DEBUG
    #
    last_decision_tick: int = 0

    #
    # STATE HELPERS
    #
    @property
    def is_busy(self) -> bool:
        return self.assigned_task is not None

    @property
    def can_move(self) -> bool:
        return self.enabled and not self.offline and not self.damaged

    @property
    def can_work(self) -> bool:
        return self.enabled and not self.offline

    #
    # STATE MANAGEMENT
    #
    def set_state(self, state: str):
        self.state = state

    #
    # TASK ASSIGNMENT
    #
    def assign_task(self, task_id: str):
        self.assigned_task = task_id
        self.state = "WORKING"

    #
    # CLEAR TASK
    #
    def clear_task(self):
        self.assigned_task = None
        self.state = "IDLE"

    #
    # DISABLE DRONE
    #
    def disable(self):
        self.enabled = False
        self.state = "DISABLED"

    #
    # ENABLE DRONE
    #
    def enable(self):
        self.enabled = True
        self.state = "IDLE"


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
    # TARGET
    #
    target_x: int | None = None
    target_y: int | None = None
    #
    # ACTIVE PATH
    #
    path: list[tuple[int, int]] = field(default_factory=list)
    #
    # NAVIGATION FLAGS
    #
    dirty: bool = False
    destination_reached: bool = False
    #
    # BLOCKING CONTROL
    #
    blocked_ticks: int = 0
    max_blocked_ticks: int = 3
    #
    # REBUILD COOLDOWN
    #
    cooldown_ticks: int = 0
    repath_cooldown: int = 5
    #
    # TARGET TRACKING
    #
    last_target: tuple[int, int] | None = None


@dataclass(slots=True)
class TaskComponent:
    current_task_id: str | None = None
    executing_task: bool = False
    cooperative: bool = False


from dataclasses import dataclass


@dataclass(slots=True)
class BatteryComponent:

    #
    # CURRENT ENERGY
    #
    level: float = 100.0
    #
    # MAX ENERGY CAPACITY
    #
    max_level: float = 100.0
    #
    # PASSIVE ENERGY DRAIN
    # used every tick
    #
    consumption_rate: float = 0.05
    #
    # EXTRA MOVEMENT DRAIN
    # optional multiplier source
    #
    movement_cost: float = 1.0
    #
    # CHARGING STATE
    #
    charging: bool = False
    #
    # LOW ENERGY THRESHOLD (%)
    #
    critical_threshold: float = 20.0
    #
    # AI STATE:
    # entity is currently searching
    # for charging station
    #
    seeking_charge: bool = False
    #
    # RESERVED CHARGING STATION ID
    #
    reserved_station: str | None = None
    #
    # BATTERY EMPTY FLAG
    #
    depleted: bool = False
    #
    # LAST CRITICAL WARNING TICK
    # prevents telemetry spam
    #
    last_warning_tick: int = -1
    #
    # ENABLE/DISABLE DRAIN
    #
    drain_enabled: bool = True

    #
    # NORMALIZED BATTERY PERCENT
    #
    @property
    def percent(self) -> float:
        if self.max_level <= 0:
            return 0.0
        return (self.level / self.max_level) * 100.0

    #
    # LOW POWER CHECK
    #
    @property
    def is_critical(self) -> bool:
        return self.percent <= self.critical_threshold

    #
    # HAS ENERGY
    #
    @property
    def has_energy(self) -> bool:
        return self.level > 0

    #
    # SAFE ENERGY CLAMP
    #
    def clamp(self):
        if self.level < 0:
            self.level = 0
        if self.level > self.max_level:
            self.level = self.max_level

    #
    # DRAIN ENERGY
    #
    def consume(self, amount: float):
        if not self.drain_enabled:
            return
        self.level -= amount
        self.clamp()
        if self.level <= 0:
            self.depleted = True

    #
    # RESTORE ENERGY
    #

    def recharge(self, amount: float):
        self.level += amount
        self.clamp()
        if self.level > 0:
            self.depleted = False


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
