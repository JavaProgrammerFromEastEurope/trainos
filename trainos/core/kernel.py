from trainos.core.config import ConfigLoader
from trainos.core.event_bus import EventBus
from trainos.core.state import SystemState
from trainos.core.telemetry import Telemetry
from trainos.core.persistence import PersistenceManager
from trainos.ecs.roles import DroneRole
from trainos.simulation.simulation_clock import SimulationClock
from trainos.simulation.tick import TickLoop
from trainos.tasks.task_manager import TaskManager
from trainos.world.world_grid import WorldGrid
from trainos.ecs.entity_manager import EntityManager
from trainos.ecs.scheduler import Scheduler
from trainos.ecs.component import (
    RoleComponent,
    SpatialComponent,
    VelocityComponent,
    NavigationComponent,
    StatusComponent,
    TaskComponent,
    BatteryComponent,
    ChargingStationComponent,
)
from trainos.ecs.systems.occupancy_system import OccupancySystem
from trainos.ecs.systems.battery_system import BatterySystem
from trainos.ecs.systems.charging_reservation_system import ChargingReservationSystem
from trainos.ecs.systems.energy_ai_system import EnergyAISystem
from trainos.ecs.systems.charging_system import ChargingSystem
from trainos.ecs.systems.task_system import TaskSystem
from trainos.ecs.systems.navigation_system import NavigationSystem
from trainos.ecs.systems.local_avoidance_system import LocalAvoidanceSystem
from trainos.ecs.systems.reservation_system import ReservationSystem
from trainos.ecs.systems.movement_system import MovementSystem
from trainos.ecs.systems.task_execution_system import TaskExecutionSystem
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
        self._spawn_test_drones()
        self._spawn_charging_station()

    def _register_systems(self):

        self.scheduler.add_task(OccupancySystem(self.world), tick_interval=1)
        self.scheduler.add_task(BatterySystem(), tick_interval=1)
        self.scheduler.add_task(ChargingReservationSystem(), tick_interval=1)
        self.scheduler.add_task(EnergyAISystem(), tick_interval=1)
        self.scheduler.add_task(ChargingSystem(), tick_interval=1)
        self.scheduler.add_task(TaskSystem(self.task_manager), tick_interval=1)
        self.scheduler.add_task(NavigationSystem(self.world), tick_interval=1)
        self.scheduler.add_task(LocalAvoidanceSystem(self.world), tick_interval=1)
        self.scheduler.add_task(ReservationSystem(self.world), tick_interval=1)
        self.scheduler.add_task(MovementSystem(), tick_interval=1)
        self.scheduler.add_task(TaskExecutionSystem(self.task_manager), tick_interval=1)
        self.scheduler.add_task(SpatialSystem(), tick_interval=1)

    def _spawn_test_drones(self):
        #
        # ENGINEER DRONE
        #
        self.scheduler.add_task(SpatialSystem(), tick_interval=1)
        engineer_id = self.entities.create_entity()
        self.entities.add_component(
            engineer_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=1, cell_y=1
            ),
        )
        self.entities.add_component(engineer_id, VelocityComponent())
        self.entities.add_component(engineer_id, NavigationComponent())
        self.entities.add_component(engineer_id, StatusComponent(active=True))
        self.entities.add_component(engineer_id, TaskComponent())
        self.entities.add_component(
            engineer_id, BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.05)
        )
        self.entities.add_component(
            engineer_id, RoleComponent(role=DroneRole.ENGINEER, efficiency=1.5)
        )
        self.telemetry.log(f"Spawned ENGINEER drone " f"{engineer_id}")
        #
        # SECOND ENGINEER DRONE
        #
        engineer2_id = self.entities.create_entity()
        self.entities.add_component(
            engineer2_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=2, cell_y=1
            ),
        )
        self.entities.add_component(engineer2_id, VelocityComponent())
        self.entities.add_component(engineer2_id, NavigationComponent())
        self.entities.add_component(engineer2_id, StatusComponent(active=True))
        self.entities.add_component(engineer2_id, TaskComponent())
        self.entities.add_component(
            engineer2_id,
            BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.05),
        )
        self.entities.add_component(
            engineer2_id, RoleComponent(role=DroneRole.ENGINEER, efficiency=1.3)
        )
        self.telemetry.log(f"Spawned ENGINEER drone " f"{engineer2_id}")
        #
        # MINER DRONE
        #
        miner_id = self.entities.create_entity()
        self.entities.add_component(
            miner_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=3, cell_y=1
            ),
        )
        self.entities.add_component(miner_id, VelocityComponent())
        self.entities.add_component(miner_id, NavigationComponent())
        self.entities.add_component(miner_id, StatusComponent(active=True))
        self.entities.add_component(miner_id, TaskComponent())
        self.entities.add_component(
            miner_id, BatteryComponent(level=100.0, max_level=100.0, drain_rate=0.06)
        )
        self.entities.add_component(
            miner_id, RoleComponent(role=DroneRole.MINER, efficiency=1.8)
        )
        self.telemetry.log(f"Spawned MINER drone " f"{miner_id}")
        #
        # HAULER DRONE
        #
        hauler_id = self.entities.create_entity()
        self.entities.add_component(
            hauler_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=4, cell_y=1
            ),
        )
        self.entities.add_component(hauler_id, VelocityComponent())
        self.entities.add_component(hauler_id, NavigationComponent())
        self.entities.add_component(hauler_id, StatusComponent(active=True))
        self.entities.add_component(hauler_id, TaskComponent())
        self.entities.add_component(
            hauler_id, BatteryComponent(level=120.0, max_level=120.0, drain_rate=0.04)
        )
        self.entities.add_component(
            hauler_id, RoleComponent(role=DroneRole.HAULER, efficiency=0.9)
        )
        self.telemetry.log(f"Spawned HAULER drone " f"{hauler_id}")
        #
        # SCOUT DRONE
        #
        scout_id = self.entities.create_entity()
        self.entities.add_component(
            scout_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=5, cell_y=1
            ),
        )
        self.entities.add_component(scout_id, VelocityComponent())
        self.entities.add_component(scout_id, NavigationComponent())
        self.entities.add_component(scout_id, StatusComponent(active=True))
        self.entities.add_component(scout_id, TaskComponent())
        self.entities.add_component(
            scout_id, BatteryComponent(level=80.0, max_level=80.0, drain_rate=0.03)
        )
        self.entities.add_component(
            scout_id, RoleComponent(role=DroneRole.SCOUT, efficiency=2.2)
        )
        self.telemetry.log(f"Spawned SCOUT drone " f"{scout_id}")

    def _spawn_charging_station(self):
        entity_id = self.entities.create_entity()
        self.entities.add_component(
            entity_id,
            SpatialComponent(
                wagon_id="wagon_001", sector_id="reactor", cell_x=2, cell_y=2
            ),
        )
        self.entities.add_component(
            entity_id, ChargingStationComponent(station_id="charger_001")
        )
        self.entities.add_component(entity_id, StatusComponent(active=True))
        self.telemetry.log(f"Spawned charging station " f"{entity_id}")

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
