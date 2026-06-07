from governor.policies.base_policy import BasePolicy
from governor.policy_actions import PolicyAction


class EmergencyPolicy(BasePolicy):

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        if state.emergency_level >= 0.8:
            return PolicyAction.DECLARE_EMERGENCY
        return None
