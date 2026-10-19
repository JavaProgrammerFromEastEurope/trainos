from kernel.workflow.policies.workflow_policy import WorkflowPolicy

from kernel.workflow.policies.policy_type 	import PolicyType
from kernel.workflow.policies.retry_policy 	import RetryPolicy
from kernel.workflow.policies.policy_engine import PolicyEngine


def test_retry_policy():

    policy = WorkflowPolicy(
        policy_id="POLICY-002",
        policy_type=PolicyType.RETRY,
        retry=RetryPolicy(
            max_attempts=3,
            delay_ticks=5,
        ),
    )
    assert PolicyEngine().should_retry(policy) is True
    assert policy.retry.max_attempts == 3
