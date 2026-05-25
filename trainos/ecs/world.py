from trainos.ecs.systems.movement_system 	import MovementSystem
from trainos.ecs.systems.battery_system 	import BatterySystem
from trainos.ecs.systems.spatial_system 	import SpatialSystem
from trainos.ecs.systems.telemetry_system import TelemetrySystem
from trainos.ecs.entity_manager 					import EntityManager
from trainos.core.scheduler 							import Scheduler


class ECSWorld:

    def __init__(self):

        self.entities 	= EntityManager()
        self.scheduler 	= Scheduler()

        self.scheduler.add_task(SpatialSystem(), 		tick_interval = 10)
        # 60hz
        self.scheduler.add_task(MovementSystem(), 	tick_interval = 1)
        # 1hz
        self.scheduler.add_task(BatterySystem(), 		tick_interval = 60)
        # 0.5hz
        self.scheduler.add_task(TelemetrySystem(), 	tick_interval = 120)

    def update(self, current_tick, telemetry):
        self.scheduler.update(current_tick, self.entities, telemetry)
