from governor.policies import (
    FoodPolicy,
    EnergyPolicy,
    CongestionPolicy,
    WorkloadPolicy,
    EmergencyPolicy,
)


class PolicyEngine:

    def __init__(self):

        self.policies = [
            # самый высокий приоритет
            EmergencyPolicy(),
            EnergyPolicy(),
            FoodPolicy(),
            CongestionPolicy(),
            WorkloadPolicy(),
        ]

    def evaluate(
        self,
        state,
        task_manager,
        traffic_system,
    ):

        actions = []

        for policy in self.policies:

            action = policy.execute(
                state,
                task_manager,
                traffic_system,
            )

            if action is not None:
                actions.append(action)

        return actions
