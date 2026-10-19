from dataclasses import dataclass

from .retry_policy import RetryPolicy
from .policy_type import PolicyType


@dataclass(frozen=True, slots=True)
class CommandPolicy:

    policy_id: str
    policy_type: PolicyType
    retry: RetryPolicy | None = None
