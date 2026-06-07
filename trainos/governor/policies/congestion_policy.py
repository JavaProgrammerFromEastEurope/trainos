from governor.policies.base_policy import BasePolicy
from governor.policy_actions import PolicyAction


class CongestionPolicy(BasePolicy):

    MAX_CONGESTION = 0.70

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        if state.congestion > self.MAX_CONGESTION:
            return PolicyAction.REDUCE_TRAFFIC
        return None
