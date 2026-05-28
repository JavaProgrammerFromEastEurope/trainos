from trainos.core.module import BaseModule
from trainos.ecs.world import ECSWorld
from trainos.ecs.component import (
    PositionComponent,
    VelocityComponent,
    BatteryComponent,
    DroneComponent,
    StatusComponent,
    SpatialComponent,
    NavigationComponent,
)


class DroneModule(BaseModule):

    def __init__(self, event_bus, telemetry, state, world):
        super().__init__("drone_module", event_bus, telemetry, state)
        self.world = ECSWorld(world)
    def start(self):
        self.telemetry.log("Drone module started")
        self._spawn_drone(
            drone_id="drone_001", start_x=0, start_y=0, target_x=9, target_y=9
        )
    def _spawn_drone(self, drone_id, start_x, start_y, target_x, target_y):
        entity = self.world.entities.create_entity()

        self.world.entities.add_component(
            entity, PositionComponent(x=float(start_x), y=float(start_y))
        )
        self.world.entities.add_component(entity, VelocityComponent(dx=0.0, dy=0.0))
        self.world.entities.add_component(entity, BatteryComponent(level=100.0, consumption_rate=0.5))
        self.world.entities.add_component(entity, DroneComponent(drone_id=drone_id))
        self.world.entities.add_component(entity, StatusComponent(active=True))
        self.world.entities.add_component(entity, NavigationComponent(target_x=target_x, target_y=target_y))
        self.world.entities.add_component(entity,
            SpatialComponent(
                wagon_id="wagon_001",
                sector_id="reactor",
                cell_x=start_x,
                cell_y=start_y,
            ))
        self.telemetry.log(f"Spawned drone " f"{drone_id}")

    def update(self, current_tick):
        self.world.update(current_tick=current_tick, telemetry=self.telemetry)

    def shutdown(self):
        self.telemetry.log("Drone module shutdown")
