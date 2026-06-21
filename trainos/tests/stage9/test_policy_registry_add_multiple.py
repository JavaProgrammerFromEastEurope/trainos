from trainos.kernel.communication.governance.policy.policy import Policy
from trainos.kernel.communication.governance.policy.policy_registry import PolicyRegistry
from trainos.kernel.communication.governance.policy.policy_type import PolicyType


def test_policy_registry_add_multiple():

    registry = PolicyRegistry()

    policy_1 = Policy(
        type=PolicyType.CONSERVATION,
    )

    policy_2 = Policy(
        type=PolicyType.EMERGENCY,
    )

    registry.add(policy_1)
    registry.add(policy_2)

    policies = registry.policies()

    assert len(policies) == 2

    assert policy_1 in policies
    assert policy_2 in policies