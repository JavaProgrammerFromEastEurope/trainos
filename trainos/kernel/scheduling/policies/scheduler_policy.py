from dataclasses import dataclass

from .policy_type import PolicyType


@dataclass(frozen=True, slots=True)
class SchedulerPolicy:

    policy_id: 		str
    policy_type: 	PolicyType