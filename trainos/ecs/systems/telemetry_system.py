from trainos.ecs.component import (
    PositionComponent,
    BatteryComponent,
    DroneComponent,
    NavigationComponent,
    StatusComponent,
)


class TelemetrySystem:

    def update(self, entity_manager, telemetry):

        #
        # COMPONENT TABLES
        #
        positions = entity_manager.get_components(PositionComponent)
        batteries = entity_manager.get_components(BatteryComponent)
        drones = entity_manager.get_components(DroneComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        statuses = entity_manager.get_components(StatusComponent)
        #
        # ITERATE DRONES
        #

        for entity_id, drone in drones.items():
            position = positions.get(entity_id)
            battery = batteries.get(entity_id)
            navigation = navigations.get(entity_id)
            status = statuses.get(entity_id)
            #
            # REQUIRED COMPONENTS
            #
            if not position:
                continue
            if not battery:
                continue
            if not status:
                continue
            #
            # TARGET
            #
            target_info = "NONE"
            if (
                navigation
                and navigation.target_x is not None
                and navigation.target_y is not None
            ):
                target_info = f"{navigation.target_x}," f"{navigation.target_y}"
            #
            # PATH LENGTH
            #
            path_length = 0
            if navigation:
                path_length = len(navigation.path)
            #
            # PRINT SNAPSHOT
            #
            print(
                f"[DRONE] "
                f"id={entity_id} "
                f"drone={drone.drone_id} "
                f"role={drone.role} "
                f"state={drone.state} "
                f"pos=({position.x},{position.y}) "
                f"battery={round(battery.level,1)}/{battery.max_level} "
                f"task={drone.assigned_task or 'IDLE'} "
                f"target={target_info} "
                f"path={path_length}"
            )
            #
            # METRICS
            #
            telemetry.metric(
                f"entity.{entity_id}.battery",
                round(battery.level, 2),
            )
            telemetry.metric(
                f"entity.{entity_id}.battery_percent",
                round(
                    battery.level / battery.max_level * 100,
                    2,
                ),
            )
            telemetry.metric(
                f"entity.{entity_id}.x",
                position.x,
            )
            telemetry.metric(
                f"entity.{entity_id}.y",
                position.y,
            )
            telemetry.metric(
                f"entity.{entity_id}.active",
                int(status.active),
            )
            telemetry.metric(
                f"entity.{entity_id}.can_move",
                int(drone.can_move),
            )
            telemetry.metric(
                f"entity.{entity_id}.busy",
                int(drone.is_busy),
            )
            if navigation:
                telemetry.metric(
                    f"entity.{entity_id}.blocked_ticks",
                    navigation.blocked_ticks,
                )
                telemetry.metric(
                    f"entity.{entity_id}.path_length",
                    len(navigation.path),
                )
                telemetry.metric(
                    f"entity.{entity_id}.destination_reached",
                    int(navigation.destination_reached),
                )
