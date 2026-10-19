from kernel.governance.policies.policy import Policy
from kernel.governance.policies.policy_engine import PolicyEngine
from kernel.governance.policies.policy_status import PolicyStatus
from kernel.governance.policies.policy_type import PolicyType


def test_policy_engine():

    engine = PolicyEngine()
    policy = Policy(
        policy_id="P1",
        decision_id="D1",
        title="Emergency Policy",
        policy_type=PolicyType.EMERGENCY,
        status=PolicyStatus.SUSPENDED,
    )

    active = engine.activate(policy)
    assert active.status == PolicyStatus.ACTIVE

    suspended = engine.suspend(active)
    assert suspended.status == PolicyStatus.SUSPENDED
