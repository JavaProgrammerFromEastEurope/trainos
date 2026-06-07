class BasePolicy:

    def enabled(self, state):
        return True

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        return None
