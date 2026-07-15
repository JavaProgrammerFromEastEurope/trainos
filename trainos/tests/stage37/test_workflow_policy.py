from kernel.workflow.policies.workflow_policy import WorkflowPolicy

from kernel.workflow.policies.policy_type 	import PolicyType
from kernel.workflow.policies.policy_engine import PolicyEngine


def test_workflow_policy():

    policy = WorkflowPolicy(
        policy_id="POLICY-001",
        policy_type=PolicyType.FAIL_FAST,
    )
    engine = PolicyEngine()
    assert engine.should_stop(policy) is True
    assert engine.should_retry(policy) is False
