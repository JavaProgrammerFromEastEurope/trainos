from governor.policies.base_policy import BasePolicy
from governor.policy_actions import PolicyAction


class FoodPolicy(BasePolicy):

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        return None
