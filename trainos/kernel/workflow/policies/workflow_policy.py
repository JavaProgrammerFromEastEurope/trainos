from dataclasses import dataclass

from .policy_type import PolicyType


@dataclass(frozen=True, slots=True)
class WorkflowPolicy:

    policy_id: str
    policy_type: PolicyType
    retry: object | None = None