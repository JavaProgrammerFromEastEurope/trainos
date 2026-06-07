from governor.policies.base_policy import BasePolicy
from governor.policy_actions import PolicyAction


class WorkloadPolicy(BasePolicy):

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        total = state.idle_drones + state.busy_drones
        if total == 0:
            return None
        utilization = state.busy_drones / total
        if utilization > 0.90:
            return PolicyAction.LIMIT_WORKLOAD
        return None
