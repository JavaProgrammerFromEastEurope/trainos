from __future__ import annotations

from .command_policy import CommandPolicy
from .policy_type import PolicyType


class PolicyEngine:
    """Evaluates command policies without performing execution itself."""

    def should_retry(self, policy: CommandPolicy) -> bool:
        return policy.policy_type is PolicyType.RETRY

    def requires_confirmation(self, policy: CommandPolicy) -> bool:
        return policy.policy_type is PolicyType.REQUIRE_CONFIRMATION
