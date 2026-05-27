from trainos.ecs.component import (
    TaskComponent,
    SpatialComponent,
    StatusComponent,
    VelocityComponent,
)


class TaskExecutionSystem:

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def update(self, entity_manager, telemetry):
        task_components = entity_manager.get_components(TaskComponent)
        spatials = entity_manager.get_components(SpatialComponent)
        statuses = entity_manager.get_components(StatusComponent)
        velocities = entity_manager.get_components(VelocityComponent)
        processed_tasks = set()

        for entity_id, task_component in task_components.items():
            current_task_id = task_component.current_task_id
            if current_task_id is None:
                continue

            if current_task_id in processed_tasks:
                continue

            status 		= statuses.get(entity_id)
            spatial 	= spatials.get(entity_id)
            velocity 	= velocities.get(entity_id)

            if not status:
                continue

            if not spatial:
                continue

            if not velocity:
                continue

            if not status.active:
                continue

            task = self.task_manager.tasks.get(current_task_id)

            if not task:
                task_component.current_task_id = None
                task_component.executing_task = False
                task_component.cooperative = False
                continue

            workers_ready = []

            for worker_id in task.assigned_entities:
                worker_spatial 		= spatials.get(worker_id)
                worker_status 		= statuses.get(worker_id)
                worker_velocity 	= velocities.get(worker_id)
                worker_task_component = task_components.get(worker_id)

                if not worker_spatial:
                    continue

                if not worker_status:
                    continue

                if not worker_velocity:
                    continue

                if not worker_task_component:
                    continue

                if not worker_status.active:
                    continue

                at_target = (
                    worker_spatial.cell_x 		== task.target_x
                    and worker_spatial.cell_y == task.target_y
                )

                if not at_target:
                    continue

                worker_velocity.dx = 0
                worker_velocity.dy = 0

                worker_task_component.executing_task = True
                workers_ready.append(worker_id)

            if not workers_ready:
                continue

            if len(workers_ready) < task.required_workers:

                telemetry.log(
                    f"Task {task.task_id} "
                    f"waiting for workers "
                    f"("
                    f"{len(workers_ready)}"
                    f"/"
                    f"{task.required_workers}"
                    f")"
                )
                continue

            if not task.started:
                task.mark_started()
                telemetry.log(
                    f"Task {task.task_id} "
                    f"started with "
                    f"{len(workers_ready)} "
                    f"workers"
                )

            worker_bonus = len(workers_ready)
            task.advance(worker_bonus)
            telemetry.metric(f"task.{task.task_id}.progress", task.progress)
            telemetry.metric(f"task.{task.task_id}.workers", len(workers_ready))
            telemetry.metric(f"task.{task.task_id}.percent", task.progress_percent)
            telemetry.log(
                f"Task {task.task_id} "
                f"progress "
                f"{task.progress}/"
                f"{task.duration}"
            )

            if task.completed:
                telemetry.log(f"Task {task.task_id} " f"completed")
                for worker_id in list(task.assigned_entities):
                    worker_task = task_components.get(worker_id)
                    if not worker_task:
                        continue
                    worker_task.current_task_id = None
                    worker_task.executing_task = False
                    worker_task.cooperative = False
                task.assigned_entities.clear()
            processed_tasks.add(current_task_id)
