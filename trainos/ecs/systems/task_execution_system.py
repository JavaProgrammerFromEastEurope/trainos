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
        spatials 		= entity_manager.get_components(SpatialComponent)
        statuses 		= entity_manager.get_components(StatusComponent)
        velocities 	= entity_manager.get_components(VelocityComponent)
        navigations = entity_manager.get_components(NavigationComponent)
        #
        # IMPORTANT
        # prevents duplicate processing
        #
        processed_tasks = set()
        #
        # ITERATE ENTITIES
        #
        for entity_id, task_component in task_components.items():
            current_task_id = task_component.current_task_id
            if current_task_id is None:
                continue
            #
            # TASK ALREADY UPDATED
            #
            if current_task_id in (processed_tasks):
                continue
            task = self.task_manager.tasks.get(current_task_id)
            #
            # TASK REMOVED
            #
            if not task:
                task_component.current_task_id = None
                task_component.executing_task = False
                task_component.cooperative = False
                continue
            #
            # READY WORKERS
            #
            workers_ready = []
            #
            # VALIDATE ALL ASSIGNED WORKERS
            #
            for worker_id in task.assigned_entities:
                worker_spatial 		= spatials.get(worker_id)
                worker_status 		= statuses.get(worker_id)
                worker_velocity 	= velocities.get(worker_id)
                worker_navigation = navigations.get(worker_id)
                worker_task = task_components.get(worker_id)
                #
                # REQUIRED COMPONENTS
                #
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
                #
                # ENTITY DISABLED
                #
                if not worker_status.active:
                    continue
                #
                # INTERACTION DISTANCE
                #
                dx = abs(worker_spatial.cell_x - task.target_x)
                dy = abs(worker_spatial.cell_y - task.target_y)
                distance = dx + dy
                at_target = distance <= task.interaction_radius
                if not at_target:
                    continue
                #
                # STOP MOVEMENT
                #
                worker_velocity.dx = 0
                worker_velocity.dy = 0
                #
                # EXECUTION MODE
                #
                worker_task.executing_task = True
                workers_ready.append(worker_id)
            #
            # NO READY WORKERS
            #
            if not workers_ready:
                processed_tasks.add(current_task_id)
                continue
            #
            # WAIT FOR MORE WORKERS
            #
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
                processed_tasks.add(current_task_id)
                continue
            #
            # START TASK
            #
            if not task.started:
                task.mark_started()
                telemetry.log(
                    f"Task {task.task_id} "
                    f"started with "
                    f"{len(workers_ready)} "
                    f"workers"
                )
            #
            # COOPERATIVE SPEED BONUS
            #
            worker_bonus = len(workers_ready)
            #
            # ADVANCE TASK
            #
            task.advance(worker_bonus)
            #
            # METRICS
            #
            telemetry.metric(f"task.{task.task_id}.progress", task.progress)
            telemetry.metric(f"task.{task.task_id}.workers", len(workers_ready))
            telemetry.metric(f"task.{task.task_id}.percent", task.progress_percent)
            telemetry.log(
                f"Task {task.task_id} "
                f"progress "
                f"{task.progress}/"
                f"{task.duration}"
            )
            #
            # TASK COMPLETED
            #
            if task.completed:
                telemetry.log(f"Task {task.task_id} " f"completed")
                #
                # RELEASE WORKERS
                #
                for worker_id in list(task.assigned_entities):
                    worker_task = task_components.get(worker_id)
                    worker_navigation = navigations.get(worker_id)
                    worker_velocity = velocities.get(worker_id)
                    if worker_task:
                        worker_task.current_task_id = None
                        worker_task.executing_task = False
                        worker_task.cooperative = False
                    #
                    # CLEAR NAVIGATION
                    #
                    if worker_navigation:
                        worker_navigation.target_x = None
                        worker_navigation.target_y = None
                        worker_navigation.path.clear()
                    #
                    # STOP MOVEMENT
                    #
                    if worker_velocity:
                        worker_velocity.dx = 0
                        worker_velocity.dy = 0
                #
                # RELEASE TASK
                #
                task.assigned_entities.clear()
            #
            # MARK PROCESSED
            #
            processed_tasks.add(current_task_id)
