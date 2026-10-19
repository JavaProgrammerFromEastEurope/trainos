from dataclasses import dataclass

from .policy_type import PolicyType


@dataclass
class Policy:
    type: PolicyType
