from governor.models.train_state import TrainState

from trainos.ecs.component import (
    DroneComponent,
    StatusComponent,
    TaskComponent,
)


class StateBuilder:

    def __init__(self):
        self.tick_counter = 0

    def build(
        self,
        entity_manager,
        task_manager,
        traffic_system,
    ):

        self.tick_counter += 1
        drones 		= entity_manager.get_components(DroneComponent)
        statuses 	= entity_manager.get_components(StatusComponent)
        tasks 		= entity_manager.get_components(TaskComponent)

        total_entities = len(statuses)

        active_entities = sum(1 for status in statuses.values() if status.active)

        total_tasks = len(task_manager.tasks)

        active_tasks = sum(
            1
            for task in task_manager.tasks.values()
            if task.started and not task.completed
        )

        idle_drones = 0
        busy_drones = 0
        battery_sum = 0.0

        for entity_id, drone in drones.items():
            battery_sum += drone.battery
            task = tasks.get(entity_id)
            if task and task.executing_task:
                busy_drones += 1
            else:
                idle_drones += 1
        average_battery = 0.0

        if drones:
            average_battery = battery_sum / len(drones)
        congestion = 0.0
        if traffic_system:
            congestion = traffic_system.global_congestion()

        return TrainState(
            tick=self.tick_counter,
            total_entities=total_entities,
            active_entities=active_entities,
            total_tasks=total_tasks,
            active_tasks=active_tasks,
            idle_drones=idle_drones,
            busy_drones=busy_drones,
            average_battery=average_battery,
            congestion=congestion,
            emergency_level=0.0,
        )
