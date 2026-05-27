from trainos.ecs.component import (
    TaskComponent,
    NavigationComponent,
    SpatialComponent,
    StatusComponent,
)


class TaskSystem:

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def update(self, entity_manager, telemetry):
        task_components = entity_manager.get_components(TaskComponent)
        navigations 		= entity_manager.get_components(NavigationComponent)
        spatials 				= entity_manager.get_components(SpatialComponent)
        statuses 				= entity_manager.get_components(StatusComponent)
        available_tasks = self.task_manager.get_available_tasks()

        for entity_id, task_component in task_components.items():
            status 			= statuses.get(entity_id)
            navigation 	= navigations.get(entity_id)
            spatial 		= spatials.get(entity_id)

            if not status:
                continue

            if not navigation:
                continue

            if not spatial:
                continue

            if not status.active:
                continue

            if task_component.current_task_id is not None:
                current_task = self.task_manager.tasks.get(
                    task_component.current_task_id
                )
                if (
                    current_task
                    and spatial.cell_x == current_task.target_x
                    and spatial.cell_y == current_task.target_y
                ):
                    current_task.completed = True
                    telemetry.log(
                        f"Entity {entity_id} "
                        f"completed task "
                        f"{current_task.task_id}"
                    )
                    task_component.current_task_id = None
                continue
            if not available_tasks:
                continue
            selected_task = available_tasks.pop(0)
            self.task_manager.assign_task(selected_task.task_id, entity_id)
            task_component.current_task_id = selected_task.task_id
            navigation.target_x = selected_task.target_x
            navigation.target_y = selected_task.target_y
            navigation.dirty = True
            telemetry.log(
                f"Entity {entity_id} " f"accepted task " f"{selected_task.task_id}"
            )
