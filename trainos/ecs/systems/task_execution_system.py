from trainos.ecs.component import (
    TaskComponent,
    SpatialComponent,
    StatusComponent,
    VelocityComponent,
    NavigationComponent,
    DroneComponent,
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
        drones = entity_manager.get_components(DroneComponent)

        #
        # PREVENT DUPLICATE PROCESSING
        #
        processed_tasks = set()

        #
        # PROCESS ENTITIES
        #
        for entity_id, task_component in task_components.items():

            current_task_id = task_component.current_task_id

            if current_task_id is None:
                continue

            if current_task_id in processed_tasks:
                continue

            task = self.task_manager.tasks.get(current_task_id)

            #
            # TASK REMOVED
            #
            if task is None:

                task_component.current_task_id = None
                task_component.executing_task = False
                task_component.cooperative = False

                drone = drones.get(entity_id)

                if drone:
                    drone.clear_task()

                processed_tasks.add(current_task_id)
                continue

            workers_ready = []

            #
            # CHECK ASSIGNED WORKERS
            #
            for worker_id in list(task.assigned_entities):

                worker_spatial = spatials.get(worker_id)
                worker_status = statuses.get(worker_id)
                worker_velocity = velocities.get(worker_id)
                worker_navigation = navigations.get(worker_id)
                worker_task = task_components.get(worker_id)
                drone = drones.get(worker_id)

                #
                # REQUIRED COMPONENTS
                #
                if (
                    worker_spatial is None
                    or worker_status is None
                    or worker_velocity is None
                    or worker_navigation is None
                    or worker_task is None
                ):
                    continue

                #
                # ENTITY DISABLED
                #
                if not worker_status.active:
                    continue

                #
                # DISTANCE TO TASK
                #
                dx = abs(worker_spatial.cell_x - task.target_x)
                dy = abs(worker_spatial.cell_y - task.target_y)

                distance = dx + dy

                #
                # NOT AT TARGET YET
                #
                if distance > task.interaction_radius:
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
                #
                # NAVIGATION STATE
                #
                worker_navigation.destination_reached = True
                #
                # DRONE STATE
                #
                if drone:
                    drone.set_state("WORKING")
                workers_ready.append(worker_id)
            #
            # NOT ENOUGH WORKERS
            #
            if len(workers_ready) < task.required_workers:
                processed_tasks.add(current_task_id)
                continue
            #
            # START TASK
            #
            if not task.started:
                task.mark_started()
                telemetry.log(
                    f"Task {task.task_id} " f"started with {len(workers_ready)} workers"
                )
            #
            # ADVANCE TASK
            #
            if not task.completed:
                task.advance(len(workers_ready))
            #
            # METRICS
            #
            telemetry.metric(
                f"task.{task.task_id}.progress",
                task.progress,
            )
            telemetry.metric(
                f"task.{task.task_id}.workers",
                len(workers_ready),
            )
            telemetry.metric(
                f"task.{task.task_id}.percent",
                task.progress_percent,
            )
            #
            # TASK COMPLETED
            #
            if task.completed:
                telemetry.log(f"Task {task.task_id} completed")
                telemetry.metric(
                    f"task.{task.task_id}.completed",
                    1,
                )
                #
                # RELEASE WORKERS
                #
                for worker_id in list(task.assigned_entities):
                    worker_task 			= task_components.get(worker_id)
                    worker_navigation = navigations.get(worker_id)
                    worker_velocity 	= velocities.get(worker_id)
                    drone = drones.get(worker_id)
                    #
                    # RESET TASK COMPONENT
                    #
                    if worker_task:
                        worker_task.current_task_id = None
                        worker_task.executing_task = False
                        worker_task.cooperative = False
                    #
                    # RESET NAVIGATION
                    #
                    if worker_navigation:
                        worker_navigation.target_x = None
                        worker_navigation.target_y = None
                        worker_navigation.path.clear()
                        worker_navigation.dirty = False
                        worker_navigation.blocked_ticks = 0
                        worker_navigation.destination_reached = False
                        worker_navigation.last_target = None
                        #
                        # OPTIONAL FIELD
                        #
                        if hasattr(worker_navigation, "cooldown"):
                            worker_navigation.cooldown = 0
                    #
                    # STOP ENTITY
                    #
                    if worker_velocity:
                        worker_velocity.dx = 0
                        worker_velocity.dy = 0
                    #
                    # RESET DRONE STATE
                    #
                    if drone:
                        drone.clear_task()
                        drone.priority = 0
                        drone.target_entity = None
                        drone.stuck = False
                #
                # RELEASE TASK
                #
                task.assigned_entities.clear()
                #
                # REMOVE TASK FROM MANAGER
                #
                self.task_manager.tasks.pop(
                    task.task_id,
                    None,
                )
            #
            # MARK TASK PROCESSED
            #
            processed_tasks.add(current_task_id)
