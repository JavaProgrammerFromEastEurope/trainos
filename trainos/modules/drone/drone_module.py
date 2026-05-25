from trainos.core.module 		import BaseModule
from trainos.ecs.world 			import ECSWorld
from trainos.ecs.component 	import (
    PositionComponent,
    VelocityComponent,
    BatteryComponent,
    DroneComponent,
    StatusComponent,
)


class DroneModule(BaseModule):

    def __init__(self, event_bus, telemetry, state):
        super().__init__("drone_module", event_bus, telemetry, state)
        self.world = ECSWorld()

    def start(self):
        self.telemetry.log("Drone module started")
        entity = self.world.entities.create_entity()
        self.world.entities.add_component(entity, DroneComponent(drone_id = "drone_001"))
        self.world.entities.add_component(entity, BatteryComponent(level = 100))
        self.world.entities.add_component(entity, PositionComponent(x = 0, y = 0))
        self.world.entities.add_component(entity, VelocityComponent(dx = 1, dy = 0))
        self.world.entities.add_component(entity, StatusComponent(active = True))

    def update(self, current_tick):
        self.world.update(current_tick, self.telemetry)

    def shutdown(self):
        self.telemetry.log("Drone module shutdown")
