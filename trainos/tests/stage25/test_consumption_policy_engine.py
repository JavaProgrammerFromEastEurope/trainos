from kernel.consumption.policies.consumption_policy import ConsumptionPolicy
from kernel.consumption.policies.consumption_policy_engine import (
    ConsumptionPolicyEngine,
)


def test_consumption_policy_engine():

    engine = ConsumptionPolicyEngine()

    policy = ConsumptionPolicy(
        policy_id="POL1",
        allow_consumption=True,
    )

    result = engine.evaluate(policy)
    assert result.allowed is True
