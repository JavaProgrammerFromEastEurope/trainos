from trainos.core.config import ConfigLoader
from trainos.core.event_bus import EventBus
from trainos.core.module_manager import ModuleManager
from trainos.core.state import SystemState
from trainos.core.telemetry import Telemetry
from trainos.core.persistence import PersistenceManager

from trainos.simulation.simulation_clock import SimulationClock
from trainos.simulation.tick import TickLoop

from trainos.world.world_grid import WorldGrid
from trainos.world.occupancy_map import OccupancyMap

from trainos.tasks.task_manager import TaskManager

from trainos.ecs.entity_manager import EntityManager
from trainos.ecs.entity_factory import EntityFactory

from trainos.ecs.systems.navigation_system import NavigationSystem
from trainos.ecs.systems.movement_system import MovementSystem
from trainos.ecs.systems.task_system import TaskSystem
from trainos.ecs.systems.task_execution_system import TaskExecutionSystem
from trainos.ecs.systems.battery_system import BatterySystem
from trainos.ecs.systems.energy_ai_system import EnergyAISystem
from trainos.ecs.systems.charging_system import ChargingSystem
from trainos.ecs.systems.charging_reservation_system import (
    ChargingReservationSystem,
)
from trainos.ecs.systems.local_avoidance_system import LocalAvoidanceSystem
from trainos.ecs.systems.telemetry_system import TelemetrySystem
from trainos.ecs.systems.occupancy_system import OccupancySystem
from trainos.ecs.systems.reservation_system import ReservationSystem
from trainos.ecs.systems.spatial_system import SpatialSystem


class Kernel:

    def __init__(self):

        #
        # WORLD
        #

        self.world = WorldGrid()

        #
        # OCCUPANCY MAP
        # IMPORTANT:
        # MUST RECEIVE WORLD REFERENCE
        #

        self.occupancy_map = OccupancyMap(self.world)

        #
        # CORE
        #

        self.config = ConfigLoader()

        self.clock = SimulationClock(
            tick_rate=60,
        )

        self.persistence = PersistenceManager()

        self.event_bus = EventBus()

        self.modules = ModuleManager()

        self.state = SystemState()

        self.telemetry = Telemetry()

        #
        # CONFIG
        #

        self.system_config = self.config.load(
            "system.yaml",
        )

        tick_rate = self.system_config.get(
            "tick_rate",
            60,
        )

        #
        # TICK LOOP
        #

        self.tick = TickLoop(
            tick_rate,
        )

        #
        # ECS
        #

        self.entity_manager = EntityManager()

        #
        # ENTITY FACTORY
        #

        self.entity_factory = EntityFactory(
            self.entity_manager,
            self.telemetry,
        )

        #
        # TASKS
        #

        self.task_manager = TaskManager()

        #
        # ECS SYSTEMS
        #

        self.task_system = TaskSystem(
            self.task_manager,
        )

        self.navigation_system = NavigationSystem(
            self.world,
            self.occupancy_map,
        )

        self.local_avoidance_system = LocalAvoidanceSystem(
            self.world,
        )

        self.reservation_system = ReservationSystem(
            self.world,
        )

        self.movement_system = MovementSystem(
            self.occupancy_map,
        )

        self.task_execution_system = TaskExecutionSystem(
            self.task_manager,
        )

        self.battery_system = BatterySystem()

        self.energy_ai_system = EnergyAISystem()

        self.charging_reservation_system = ChargingReservationSystem()

        self.charging_system = ChargingSystem()

        self.occupancy_system = OccupancySystem(
            self.world,
        )

        self.spatial_system = SpatialSystem()

        self.telemetry_system = TelemetrySystem()

    def boot(self):

        #
        # STARTUP LOG
        #

        self.telemetry.log(
            "Kernel booting",
        )

        #
        # START MODULES
        #

        self.modules.start_all()

        #
        # START TICK LOOP
        #

        self.tick.run(
            self.update,
        )

    def update(self):

        #
        # CLOCK STEP
        #

        self.clock.step()

        current_tick = self.clock.current_tick()

        #
        # ECS UPDATE ORDER
        #
        # IMPORTANT:
        # ORDER IS CRITICAL
        #

        #
        # TASK ASSIGNMENT
        #

        self.task_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # ENERGY AI
        # OVERRIDES TASKS IF LOW BATTERY
        #

        self.energy_ai_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # CHARGING STATION RESERVATION
        #

        self.charging_reservation_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # PATHFINDING
        #

        self.navigation_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # LOCAL COLLISION AVOIDANCE
        #

        self.local_avoidance_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # CELL RESERVATIONS
        #

        self.reservation_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # APPLY MOVEMENT
        #

        self.movement_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # WORLD OCCUPANCY
        #

        self.occupancy_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # TASK EXECUTION
        #

        self.task_execution_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # BATTERY UPDATE
        #

        self.battery_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # CHARGING PROCESS
        #

        self.charging_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # SPATIAL METRICS
        #

        self.spatial_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # DEBUG TELEMETRY
        #

        self.telemetry_system.update(
            self.entity_manager,
            self.telemetry,
        )

        #
        # MODULES
        #

        self.modules.update_all(
            current_tick,
        )

    def shutdown(self):

        #
        # SHUTDOWN LOG
        #

        self.telemetry.log(
            "Kernel shutdown",
        )

        #
        # STOP TICK LOOP
        #

        self.tick.stop()

        #
        # SHUTDOWN MODULES
        #

        self.modules.shutdown_all()
