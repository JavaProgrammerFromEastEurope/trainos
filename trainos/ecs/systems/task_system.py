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
        spatials 				= entity_manager.get_components(SpatialComponent)
        navigations 		= entity_manager.get_components(NavigationComponent)
        statuses 				= entity_manager.get_components(StatusComponent)
        drones 					= entity_manager.get_components(DroneComponent)
        #
        # AVAILABLE TASKS
        #
        available_tasks = self.task_manager.get_available_tasks()
        #
        # NO TASKS
        #
        if not available_tasks:
            return
        #
        # PROCESS ENTITIES
        #
        for entity_id, task_component in task_components.items():
            #
            # ALREADY BUSY
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
            # FIND BEST TASK
            #
            selected_task = None
            for task in available_tasks:
                #
                # TASK FULL
                #
                if len(task.assigned_entities) >= task.required_workers:
                    continue
                #
                # ROLE CHECK
                #
                if task.required_role is not None:
                    if drone.role != task.required_role:
                        continue
                #
                # ACCEPT TASK
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
                entity_id, selected_task.task_id
            )
            if not success:
                continue
            #
            # UPDATE ENTITY TASK
            #
            task_component.current_task_id = selected_task.task_id
            task_component.executing_task = False
            task_component.cooperative = selected_task.required_workers > 1
            #
            # NAVIGATION TARGET
            #
            navigation.target_x = selected_task.target_x
            navigation.target_y = selected_task.target_y
            #
            # FORCE PATH REBUILD
            #
            navigation.path.clear()
            navigation.dirty = True
            #
            # LOG
            #
            telemetry.log(
                f"Entity {entity_id} " f"accepted task " f"{selected_task.task_id}"
            )
