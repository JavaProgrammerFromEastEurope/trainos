from .policy_type import PolicyType


class PolicyEngine:

    def should_retry(
        self,
        policy,
    ) -> bool:
        return policy.policy_type == PolicyType.RETRY

    def should_stop(
        self,
        policy,
    ) -> bool:
        return policy.policy_type == PolicyType.FAIL_FAST
