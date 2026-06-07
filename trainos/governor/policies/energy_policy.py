from governor.policies.base_policy import BasePolicy
from governor.policy_actions import PolicyAction


class EnergyPolicy(BasePolicy):

    LOW_POWER_LEVEL = 30.0

    def execute(
        self,
        state,
        task_manager,
        traffic_system,
    ):
        if state.average_battery < self.LOW_POWER_LEVEL:
            return PolicyAction.BOOST_POWER
        return None
