from dataclasses import dataclass

from kernel.governance.policies.policy_status import PolicyStatus


@dataclass(frozen=True, slots=True)
class PolicySnapshot:

    policy_id: str
    status: PolicyStatus
