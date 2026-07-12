from dataclasses import dataclass

from .policy_status import PolicyStatus
from .policy_type 	import PolicyType


@dataclass(frozen=True, slots=True)
class Policy:

    policy_id: 		str
    decision_id: 	str
    title: 				str
    policy_type: PolicyType
    status: PolicyStatus