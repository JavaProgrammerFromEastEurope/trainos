from trainos.ecs.component import (
    TaskComponent,
    SpatialComponent,
    NavigationComponent,
    StatusComponent,
    DroneComponent,
)


class TaskSystem:

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def update(self, entity_manager, telemetry):

        #
        # COMPONENT TABLES
        #
        task_components = entity_manager.get_components(TaskComponent)
        spatials = entity_manager.get_components(SpatialComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        statuses = entity_manager.get_components(StatusComponent)
        drones = entity_manager.get_components(DroneComponent)

        #
        # PROCESS ENTITIES
        #
        for entity_id, task_component in task_components.items():

            #
            # ENTITY ALREADY BUSY
            #
            if task_component.current_task_id is not None:
                continue

            #
            # REQUIRED COMPONENTS
            #
            status = statuses.get(entity_id)
            spatial = spatials.get(entity_id)
            navigation = navigations.get(entity_id)
            drone = drones.get(entity_id)

            if not status:
                continue

            if not spatial:
                continue

            if not navigation:
                continue

            if not drone:
                continue

            #
            # ENTITY DISABLED
            #
            if not status.active:
                continue

            #
            # REFRESH TASK LIST EACH ENTITY
            # IMPORTANT FIX
            #
            available_tasks = self.task_manager.get_available_tasks()

            if not available_tasks:
                break

            #
            # FIND BEST TASK
            #
            selected_task = None

            for task in available_tasks:

                #
                # TASK COMPLETE
                #
                if task.completed:
                    continue

                #
                # TASK FULL
                #
                if len(task.assigned_entities) >= task.required_workers:
                    continue

                #
                # ALREADY ASSIGNED
                #
                if entity_id in task.assigned_entities:
                    continue

                #
                # ROLE VALIDATION
                #
                if task.required_role is not None:
                    if drone.role != task.required_role:
                        continue

                #
                # TASK ACCEPTED
                #
                selected_task = task
                break

            #
            # NOTHING FOUND
            #
            if not selected_task:
                continue

            #
            # ASSIGN ENTITY
            #
            success = self.task_manager.assign_entity_to_task(
                entity_id,
                selected_task.task_id,
            )

            if not success:
                continue

            #
            # UPDATE TASK COMPONENT
            #
            task_component.current_task_id = selected_task.task_id
            task_component.executing_task = False

            #
            # NAVIGATION TARGET
            #
            target_changed = (
                navigation.target_x != selected_task.target_x
                or navigation.target_y != selected_task.target_y
            )

            navigation.target_x = selected_task.target_x
            navigation.target_y = selected_task.target_y

            #
            # REBUILD ONLY ON TARGET CHANGE
            #
            if target_changed:
                navigation.dirty = True
                navigation.destination_reached = False

            #
            # LOGGING
            #
            telemetry.log(f"Entity {entity_id} accepted task {selected_task.task_id}")

            telemetry.metric(
                f"entity.{entity_id}.task",
                selected_task.task_id,
            )
