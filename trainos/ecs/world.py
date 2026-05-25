from trainos.ecs.systems.movement_system 	import MovementSystem
from trainos.ecs.systems.battery_system 	import BatterySystem
from trainos.ecs.systems.telemetry_system import TelemetrySystem
from trainos.ecs.entity_manager 					import EntityManager

class ECSWorld:

    def __init__(self):
        self.entities = EntityManager()
        self.systems 	= [MovementSystem(), BatterySystem(), TelemetrySystem()]

    def update(self, telemetry):
        for system in self.systems:
            system.update(self.entities, telemetry)
