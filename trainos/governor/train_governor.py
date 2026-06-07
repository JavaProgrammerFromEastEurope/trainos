class TrainGovernor:

    def __init__(
        self,
        state_builder,
        policy_engine,
    ):
        self.state_builder = state_builder
        self.policy_engine = policy_engine

    def tick(
        self,
        entity_manager,
        task_manager,
        traffic_system,
    ):
        state = self.state_builder.build(
            entity_manager,
            task_manager,
            traffic_system,
        )
        actions = self.policy_engine.evaluate(
            state,
            task_manager,
            traffic_system,
        )
        return actions
