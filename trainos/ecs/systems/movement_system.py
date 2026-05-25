from trainos.ecs.component import (
    PositionComponent,
    VelocityComponent,
    BatteryComponent,
    StatusComponent,
)


class MovementSystem:

    def update(self, entity_manager, telemetry):

        positions 	= entity_manager.get_components(PositionComponent)

        velocities 	= entity_manager.get_components(VelocityComponent)

        batteries 	= entity_manager.get_components(BatteryComponent)

        statuses 		= entity_manager.get_components(StatusComponent)

        for entity_id, position in positions.items():

            velocity 	= velocities.get(entity_id)

            battery 	= batteries.get(entity_id)

            status 		= statuses.get(entity_id)

            if not velocity:
                continue

            if not battery:
                continue

            if not status:
                continue

            if not status.active:
                continue

            if battery.level <= 0:
                continue

            new_x = position.x + velocity.dx
            new_y = position.y + velocity.dy

            WORLD_WIDTH = 100
            WORLD_HEIGHT = 100

            if new_x < 0 or new_x > WORLD_WIDTH:
                continue

            if new_y < 0 or new_y > WORLD_HEIGHT:
                continue

            position.x = new_x
            position.y = new_y

            battery.level -= battery.consumption_rate

            telemetry.metric(f"entity.{entity_id}.x", position.x)

            telemetry.metric(f"entity.{entity_id}.y", position.y)
