class InterruptionHandler:

    def should_interrupt(self, current_task, world_state):
        if world_state.emergency_level > 80:
            return True
        if current_task["type"] == "MOVE_POPULATION":
            return False
        if world_state.oxygen_global < 60:
            return True
        return False

    def handle(self, executor, reason):
        executor.cancel_current_tasks()
        executor.switch_mode("EMERGENCY")
        return True

