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


class Kernel:

    def __init__(self):

        #
        # WORLD
        #

        self.world = WorldGrid()

        self.occupancy_map = OccupancyMap()

        #
        # CORE
        #

        self.config = ConfigLoader()

        self.clock = SimulationClock(tick_rate=60)

        self.persistence = PersistenceManager()

        self.event_bus = EventBus()

        self.modules = ModuleManager()

        self.state = SystemState()

        self.telemetry = Telemetry()

        #
        # CONFIG
        #

        self.system_config = self.config.load("system.yaml")

        tick_rate = self.system_config["tick_rate"]

        #
        # TICK LOOP
        #

        self.tick = TickLoop(tick_rate)

        #
        # ECS
        #

        self.entity_manager = EntityManager()

        #
        # ENTITY FACTORY
        #

        self.entity_factory = EntityFactory(self.entity_manager, self.telemetry)

        #
        # TASKS
        #

        self.task_manager = TaskManager()

        #
        # ECS SYSTEMS
        #

        self.task_system = TaskSystem(self.task_manager)

        self.navigation_system = NavigationSystem(self.world, self.occupancy_map)

        self.movement_system = MovementSystem(self.occupancy_map)

        self.task_execution_system = TaskExecutionSystem(self.task_manager)

        self.battery_system = BatterySystem()

        self.energy_ai_system = EnergyAISystem()

    def boot(self):

        self.telemetry.log("Kernel booting")

        self.modules.start_all()

        self.tick.run(self.update)

    def update(self):

        #
        # CLOCK
        #

        self.clock.step()

        current_tick = self.clock.current_tick()

        #
        # ECS UPDATE ORDER
        #

        self.task_system.update(self.entity_manager, self.telemetry)

        self.navigation_system.update(self.entity_manager, self.telemetry)

        self.movement_system.update(self.entity_manager, self.telemetry)

        self.task_execution_system.update(self.entity_manager, self.telemetry)

        self.battery_system.update(self.entity_manager, self.telemetry)

        self.energy_ai_system.update(self.entity_manager, self.telemetry)

        #
        # MODULES
        #

        self.modules.update_all(current_tick)

    def shutdown(self):

        self.telemetry.log("Kernel shutdown")

        self.tick.stop()

        self.modules.shutdown_all()
