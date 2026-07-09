from .consumption_policy import ConsumptionPolicy
from .consumption_policy_result import ConsumptionPolicyResult


class ConsumptionPolicyEngine:

    def evaluate(
        self,
        policy: ConsumptionPolicy,
    ) -> ConsumptionPolicyResult:
        if not policy.allow_consumption:
            return ConsumptionPolicyResult(
                allowed=False,
                reason="Consumption disabled",
            )
        return ConsumptionPolicyResult(
            allowed=True,
        )