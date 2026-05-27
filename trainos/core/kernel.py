from trainos.core.config import ConfigLoader
from trainos.core.event_bus import EventBus
from trainos.core.state import SystemState
from trainos.core.telemetry import Telemetry
from trainos.core.persistence import PersistenceManager
from trainos.simulation.simulation_clock import SimulationClock
from trainos.simulation.tick import TickLoop
from trainos.tasks.task_manager import TaskManager
from trainos.world.world_grid import WorldGrid
from trainos.ecs.entity_manager import EntityManager
from trainos.ecs.scheduler import Scheduler
from trainos.ecs.component import (
    SpatialComponent,
    VelocityComponent,
    NavigationComponent,
    StatusComponent,
    TaskComponent,
)

from trainos.ecs.systems.task_system import TaskSystem
from trainos.ecs.systems.navigation_system import NavigationSystem
from trainos.ecs.systems.local_avoidance_system import LocalAvoidanceSystem
from trainos.ecs.systems.reservation_system import ReservationSystem
from trainos.ecs.systems.movement_system import MovementSystem
from trainos.ecs.systems.occupancy_system import OccupancySystem
from trainos.ecs.systems.spatial_system import SpatialSystem


class Kernel:

    def __init__(self):
        self.world = WorldGrid()
        self.config = ConfigLoader()
        self.clock = SimulationClock(tick_rate=60)
        self.persistence = PersistenceManager()
        self.system_config = self.config.load("system.yaml")
        self.event_bus = EventBus()
        self.state = SystemState()
        self.telemetry = Telemetry()
        tick_rate = self.system_config["tick_rate"]
        self.tick = TickLoop(tick_rate)
        self.task_manager = TaskManager()
        self.entities = EntityManager()
        self.scheduler = Scheduler()
        self._register_systems()
        self._spawn_test_drone()

    def _register_systems(self):
        self.scheduler.add_task(OccupancySystem(self.world), tick_interval=1)
        self.scheduler.add_task(TaskSystem(self.task_manager), tick_interval=1)
        self.scheduler.add_task(NavigationSystem(self.world), tick_interval=1)
        self.scheduler.add_task(LocalAvoidanceSystem(self.world), tick_interval=1)
        self.scheduler.add_task(ReservationSystem(self.world), tick_interval=1)
        self.scheduler.add_task(MovementSystem(), tick_interval=1)
        self.scheduler.add_task(SpatialSystem(), tick_interval=1)

    def _spawn_test_drone(self):
        entity_id = self.entities.create_entity()
        self.entities.add_component(
            entity_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=1, cell_y=1
            ),
        )

        self.entities.add_component(entity_id, VelocityComponent())
        self.entities.add_component(entity_id, NavigationComponent())
        self.entities.add_component(entity_id, StatusComponent(active=True))
        self.entities.add_component(entity_id, TaskComponent())
        self.telemetry.log(f"Spawned drone " f"{entity_id}")

    def boot(self):
        self.telemetry.log("Kernel booting")
        self.tick.run(self.update)

    def update(self):
        self.clock.step()
        current_tick = self.clock.current_tick()
        self.scheduler.update(current_tick, self.entities, self.telemetry)

    def shutdown(self):
        self.telemetry.log("Kernel shutdown")
        self.tick.stop()
