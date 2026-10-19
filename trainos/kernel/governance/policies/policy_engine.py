from .policy import Policy
from .policy_status import PolicyStatus


class PolicyEngine:

    def activate(
        self,
        policy: Policy,
    ) -> Policy:
        return Policy(
            policy_id=policy.policy_id,
            decision_id=policy.decision_id,
            title=policy.title,
            policy_type=policy.policy_type,
            status=PolicyStatus.ACTIVE,
        )

    def suspend(
        self,
        policy: Policy,
    ) -> Policy:
        return Policy(
            policy_id=policy.policy_id,
            decision_id=policy.decision_id,
            title=policy.title,
            policy_type=policy.policy_type,
            status=PolicyStatus.SUSPENDED,
        )