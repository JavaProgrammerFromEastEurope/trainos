from trainos.ecs.component import (
    PositionComponent,
    BatteryComponent,
    DroneComponent,
    NavigationComponent,
    TaskComponent,
    StatusComponent,
)


class TelemetrySystem:

    def __init__(self):
        #
        # REDUCE LOG SPAM
        #
        self.last_snapshot_tick = -1

    def update(self, entity_manager, telemetry):
        #
        # COMPONENT TABLES
        #
        positions = entity_manager.get_components(PositionComponent)
        batteries = entity_manager.get_components(BatteryComponent)
        drones = entity_manager.get_components(DroneComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        tasks = entity_manager.get_components(TaskComponent)
        statuses = entity_manager.get_components(StatusComponent)
        #
        # ITERATE DRONES
        #
        for entity_id, drone in drones.items():
            #
            # REQUIRED COMPONENTS
            #
            position 		= positions.get(entity_id)
            battery 		= batteries.get(entity_id)
            navigation 	= navigations.get(entity_id)
            task 				= tasks.get(entity_id)
            status 			= statuses.get(entity_id)

            if not position:
                continue
            if not battery:
                continue
            if not status:
                continue
            #
            # ENTITY STATE
            #
            state = "ACTIVE"
            if not status.active:
                state = "DISABLED"
            elif battery.charging:
                state = "CHARGING"
            elif battery.seeking_charge:
                state = "SEEKING_CHARGE"
            elif task and task.executing_task:
                state = "WORKING"
            elif navigation and navigation.moving:
                state = "MOVING"
            #
            # TARGET INFO
            #
            target_info = "NONE"
            if navigation and navigation.target:
                target_info = f"{navigation.target_x}," f"{navigation.target_y}"
            #
            # TASK INFO
            #
            task_info = "IDLE"
            if task and task.current_task_id:
                task_info = task.current_task_id
            #
            # PATH INFO
            #
            path_length = 0
            if navigation and navigation.path:
                path_length = len(navigation.path)
            #
            # OUTPUT
            #
            print(
                f"[DRONE] "
                f"id={entity_id} "
                f"drone={drone.drone_id} "
                f"role={drone.role} "
                f"state={state} "
                f"pos=({position.x},{position.y}) "
                f"battery={round(battery.level, 1)}% "
                f"task={task_info} "
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
            if navigation:
                telemetry.metric(
                    f"entity.{entity_id}.blocked_ticks",
                    navigation.blocked_ticks,
                )
                telemetry.metric(
                    f"entity.{entity_id}.path_length",
                    path_length,
                )
