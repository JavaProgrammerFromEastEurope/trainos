from trainos.ecs.component import SpatialComponent, VelocityComponent, StatusComponent


class LocalAvoidanceSystem:

    def __init__(self, world):
        self.world = world

    def update(self, entity_manager, telemetry):
        spatials 		= entity_manager.get_components(SpatialComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        spatial_lookup = {}

        for entity_id, spatial in spatials.items():
            spatial_lookup[
                (spatial.wagon_id, spatial.sector_id, spatial.cell_x, spatial.cell_y)
            ] = entity_id

        for entity_id, spatial in spatials.items():
            velocity 	= velocities.get(entity_id)
            status 		= statuses.get(entity_id)

            if not velocity:
                continue

            if not status:
                continue

            if not status.active:
                continue

            next_x = spatial.cell_x + int(velocity.dx)
            next_y = spatial.cell_y + int(velocity.dy)

            blocking_entity = spatial_lookup.get(
                (spatial.wagon_id, spatial.sector_id, next_x, next_y)
            )

            if not blocking_entity:
                continue

            blocking_velocity = velocities.get(blocking_entity)

            blocking_spatial = spatials.get(blocking_entity)

            if not blocking_velocity:
                continue

            if not blocking_spatial:
                continue

            blocking_next_x = blocking_spatial.cell_x + int(blocking_velocity.dx)
            blocking_next_y = blocking_spatial.cell_y + int(blocking_velocity.dy)

            if blocking_next_x == spatial.cell_x and blocking_next_y == spatial.cell_y:
                if entity_id > blocking_entity:
                    velocity.dx = 0
                    velocity.dy = 0
                    telemetry.log(
                        f"Entity {entity_id} " f"yielding to " f"{blocking_entity}"
                    )
