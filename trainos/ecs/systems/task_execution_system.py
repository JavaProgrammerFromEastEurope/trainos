from trainos.ecs.component import (
    TaskComponent,
    SpatialComponent,
    StatusComponent,
    VelocityComponent,
    NavigationComponent,
)


class TaskExecutionSystem:

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def update(self, entity_manager, telemetry):

        task_components = entity_manager.get_components(TaskComponent)
        spatials = entity_manager.get_components(SpatialComponent)
        statuses = entity_manager.get_components(StatusComponent)
        velocities = entity_manager.get_components(VelocityComponent)
        navigations = entity_manager.get_components(NavigationComponent)

        # ---------------------------------------------
        # TASK PROCESS LOCK (prevents double execution)
        # ---------------------------------------------
        processed_tasks = set()

        for entity_id, task_component in task_components.items():

            current_task_id = task_component.current_task_id

            if current_task_id is None:
                continue

            if current_task_id in processed_tasks:
                continue

            task = self.task_manager.tasks.get(current_task_id)

            if not task:
                task_component.current_task_id = None
                task_component.executing_task = False
                task_component.cooperative = False
                continue

            workers_ready = []

            # -----------------------------------------
            # VALIDATE ASSIGNED WORKERS
            # -----------------------------------------
            for worker_id in task.assigned_entities:

                worker_spatial = spatials.get(worker_id)
                worker_status = statuses.get(worker_id)
                worker_velocity = velocities.get(worker_id)
                worker_navigation = navigations.get(worker_id)
                worker_task = task_components.get(worker_id)

                if not worker_spatial:
                    continue
                if not worker_status:
                    continue
                if not worker_velocity:
                    continue
                if not worker_navigation:
                    continue
                if not worker_task:
                    continue

                if not worker_status.active:
                    continue

                dx = abs(worker_spatial.cell_x - task.target_x)
                dy = abs(worker_spatial.cell_y - task.target_y)
                distance = dx + dy

                at_target = distance <= task.interaction_radius

                if not at_target:
                    continue

                worker_velocity.dx = 0
                worker_velocity.dy = 0

                worker_task.executing_task = True

                workers_ready.append(worker_id)

            # -----------------------------------------
            # NO WORKERS READY
            # -----------------------------------------
            if not workers_ready:
                processed_tasks.add(current_task_id)
                continue

            # -----------------------------------------
            # WAITING FOR MORE WORKERS
            # -----------------------------------------
            if len(workers_ready) < task.required_workers:
                telemetry.log(
                    f"Task {task.task_id} waiting for workers "
                    f"({len(workers_ready)}/{task.required_workers})"
                )
                processed_tasks.add(current_task_id)
                continue

            # -----------------------------------------
            # START TASK (ONLY ONCE)
            # -----------------------------------------
            if not task.started:
                task.mark_started()
                telemetry.log(
                    f"Task {task.task_id} started with {len(workers_ready)} workers"
                )

            # -----------------------------------------
            # PROGRESS UPDATE
            # -----------------------------------------
            worker_bonus = len(workers_ready)
            task.advance(worker_bonus)

            telemetry.metric(f"task.{task.task_id}.progress", task.progress)
            telemetry.metric(f"task.{task.task_id}.workers", len(workers_ready))
            telemetry.metric(f"task.{task.task_id}.percent", task.progress_percent)

            telemetry.log(
                f"Task {task.task_id} progress {task.progress}/{task.duration}"
            )

            # -----------------------------------------
            # COMPLETION
            # -----------------------------------------
            if task.completed:

                telemetry.log(f"Task {task.task_id} completed")

                for worker_id in list(task.assigned_entities):

                    worker_task = task_components.get(worker_id)
                    worker_navigation = navigations.get(worker_id)
                    worker_velocity = velocities.get(worker_id)

                    if worker_task:
                        worker_task.current_task_id = None
                        worker_task.executing_task = False
                        worker_task.cooperative = False

                    if worker_navigation:
                        worker_navigation.target_x = None
                        worker_navigation.target_y = None
                        worker_navigation.path.clear()
                        worker_navigation.dirty = True

                    if worker_velocity:
                        worker_velocity.dx = 0
                        worker_velocity.dy = 0

                task.assigned_entities.clear()

            processed_tasks.add(current_task_id)
