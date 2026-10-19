from kernel.scheduling.policies.scheduler_policy import SchedulerPolicy

from kernel.scheduling.policies.policy_type import PolicyType
from kernel.scheduling.policies.policy_engine import PolicyEngine


def test_scheduler_policy():
    policy = SchedulerPolicy(
        policy_id="POLICY-001",
        policy_type=PolicyType.PRIORITY,
    )
    result = PolicyEngine().select(policy)
    assert result.policy_type == PolicyType.PRIORITY
