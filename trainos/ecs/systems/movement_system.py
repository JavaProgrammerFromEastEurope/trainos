from trainos.ecs.component import (
    PositionComponent,
    SpatialComponent,
    VelocityComponent,
    BatteryComponent,
    StatusComponent,
)


class MovementSystem:

    def __init__(self, occupancy_map):
        self.occupancy_map = occupancy_map

    def update(self, entity_manager, telemetry):
        positions 	= entity_manager.get_components(PositionComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        batteries 	= entity_manager.get_components(BatteryComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        spatials 		= entity_manager.get_components(SpatialComponent)
        #
        # REBUILD OCCUPANCY MAP
        #
        self.occupancy_map.clear()
        for entity_id, spatial in spatials.items():
            self.occupancy_map.occupy(spatial.cell_x, spatial.cell_y, entity_id)
        #
        # PROCESS MOVEMENT
        #
        for entity_id, position in positions.items():
            velocity 	= velocities.get(entity_id)
            battery 	= batteries.get(entity_id)
            status 		= statuses.get(entity_id)
            spatial 	= spatials.get(entity_id)
            if not velocity:
                continue
            if not battery:
                continue
            if not status:
                continue
            if not spatial:
                continue
            if not status.active:
                continue
            #
            # NO ENERGY
            #
            if battery.level <= 0:
                velocity.dx = 0
                velocity.dy = 0
                continue
            #
            # NO MOVEMENT
            #
            if velocity.dx == 0 and velocity.dy == 0:
                continue
            #
            # TARGET POSITION
            #
            new_x = spatial.cell_x + velocity.dx
            new_y = spatial.cell_y + velocity.dy
            #
            # CELL OCCUPIED
            #
            occupied = self.occupancy_map.get_entity(new_x, new_y)
            if occupied is not None:
                if occupied != entity_id:
                    velocity.dx = 0
                    velocity.dy = 0
                    telemetry.log(
                        f"Entity {entity_id} " f"blocked by " f"entity {occupied}"
                    )
                    continue
            #
            # RELEASE OLD CELL
            #
            self.occupancy_map.release(spatial.cell_x, spatial.cell_y)
            #
            # APPLY MOVEMENT
            #
            position.x = new_x
            position.y = new_y
            spatial.cell_x = new_x
            spatial.cell_y = new_y
            #
            # OCCUPY NEW CELL
            #
            self.occupancy_map.occupy(new_x, new_y, entity_id)
            #
            # ENERGY DRAIN
            #
            battery.level -= battery.consumption_rate
            if battery.level < 0:
                battery.level = 0
            #
            # MOVEMENT LOG
            #
            telemetry.log(f"Entity {entity_id} " f"moved to " f"({new_x}, {new_y})")
            telemetry.metric(f"entity.{entity_id}.x", new_x)
            telemetry.metric(f"entity.{entity_id}.y", new_y)
