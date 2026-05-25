class ScheduledTask:

    def __init__(self, system, tick_interval):
        self.system = system
        self.tick_interval = tick_interval
        self.last_tick = 0


class Scheduler:

    def __init__(self):
        self.tasks = []

    def add_task(self, system, tick_interval):
        self.tasks.append(ScheduledTask(system, tick_interval))

    def update(self, current_tick, entity_manager, telemetry):
        for task in self.tasks:
            if current_tick - task.last_tick >= task.tick_interval:
                task.system.update(entity_manager, telemetry)
                task.last_tick = current_tick
