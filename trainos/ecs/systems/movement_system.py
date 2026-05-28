from trainos.ecs.component import (
    PositionComponent,
    SpatialComponent,
    VelocityComponent,
    BatteryComponent,
    StatusComponent,
    NavigationComponent,
)


class MovementSystem:

    def __init__(self, occupancy_map):
        self.occupancy_map = occupancy_map

    def update(self, entity_manager, telemetry):

        positions = entity_manager.get_components(PositionComponent)
        velocities = entity_manager.get_components(VelocityComponent)
        batteries = entity_manager.get_components(BatteryComponent)
        statuses = entity_manager.get_components(StatusComponent)
        spatials = entity_manager.get_components(SpatialComponent)
        navigations = entity_manager.get_components(NavigationComponent)

        # --------------------------------------------------
        # DO NOT FULL CLEAR WORLD EVERY FRAME (FIX #1)
        # --------------------------------------------------
        # occupancy_map should already be maintained incrementally
        # --------------------------------------------------

        for entity_id, spatial in spatials.items():

            position = positions.get(entity_id)
            velocity = velocities.get(entity_id)
            battery = batteries.get(entity_id)
            status = statuses.get(entity_id)
            nav = navigations.get(entity_id)

            # --------------------------------------------------
            # VALIDATION
            # --------------------------------------------------
            if not position or not velocity or not battery or not status:
                continue

            if not status.active:
                continue

            if battery.level <= 0:
                velocity.dx = 0
                velocity.dy = 0
                continue

            # --------------------------------------------------
            # NO NAVIGATION → IDLE
            # --------------------------------------------------
            if not nav or not nav.path:
                velocity.dx = 0
                velocity.dy = 0
                continue

            # --------------------------------------------------
            # COOLDOWN FOR BLOCKED PATH (FIX #2)
            # --------------------------------------------------
            if nav.blocked_ticks > 5:
                nav.dirty = True
                nav.blocked_ticks = 0
                velocity.dx = 0
                velocity.dy = 0
                continue

            # --------------------------------------------------
            # NEXT STEP
            # --------------------------------------------------
            next_cell = nav.path[0]
            new_x, new_y = next_cell

            # --------------------------------------------------
            # OCCUPANCY CHECK
            # --------------------------------------------------
            occupied = self.occupancy_map.get_entity(new_x, new_y)

            if occupied is not None and occupied != entity_id:
                velocity.dx = 0
                velocity.dy = 0
                nav.blocked_ticks += 1

                telemetry.log(f"Entity {entity_id} blocked at {new_x},{new_y}")
                continue

            # --------------------------------------------------
            # MOVE ENTITY
            # --------------------------------------------------
            self.occupancy_map.release(
                spatial.cell_x,
                spatial.cell_y,
            )

            position.x = new_x
            position.y = new_y

            spatial.cell_x = new_x
            spatial.cell_y = new_y

            nav.path.pop(0)
            nav.blocked_ticks = 0

            self.occupancy_map.occupy(
                new_x,
                new_y,
                entity_id,
            )

            # --------------------------------------------------
            # ENERGY DRAIN
            # --------------------------------------------------
            battery.level -= battery.consumption_rate
            if battery.level < 0:
                battery.level = 0

            # --------------------------------------------------
            # METRICS (light)
            # --------------------------------------------------
            telemetry.metric(f"entity.{entity_id}.x", new_x)
            telemetry.metric(f"entity.{entity_id}.y", new_y)

            # --------------------------------------------------
            # DESTINATION CHECK
            # --------------------------------------------------
            if not nav.path:
                nav.destination_reached = True
                nav.dirty = False
