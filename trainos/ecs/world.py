from trainos.ecs.systems.navigation_system import NavigationSystem
from trainos.ecs.entity_manager 					import EntityManager
from trainos.core.scheduler 							import Scheduler
from trainos.ecs.systems.movement_system 	import MovementSystem
from trainos.ecs.systems.battery_system 	import BatterySystem
from trainos.ecs.systems.occupancy_system import OccupancySystem
from trainos.ecs.systems.telemetry_system import TelemetrySystem
from trainos.ecs.systems.spatial_system 	import SpatialSystem


class ECSWorld:

    def __init__(self, world):
        self.world = world
        self.entities 	= EntityManager()
        self.scheduler 	= Scheduler()
        self._register_systems()

    def _register_systems(self):
        self.scheduler.add_task(OccupancySystem(self.world),	tick_interval=1)
        # Navigation AI
        self.scheduler.add_task(NavigationSystem(self.world), tick_interval=10)
        # Physical movement
        self.scheduler.add_task(MovementSystem(), tick_interval=1)
        # Spatial synchronization
        self.scheduler.add_task(SpatialSystem(), tick_interval=10)
        # Battery management
        self.scheduler.add_task(BatterySystem(), tick_interval=60)
        # Debug telemetry
        self.scheduler.add_task(TelemetrySystem(), tick_interval=1)

    def update(self, current_tick, telemetry):
        self.scheduler.update(
            current_tick=current_tick, entity_manager=self.entities, telemetry=telemetry
        )
