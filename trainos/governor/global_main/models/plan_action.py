from dataclasses import dataclass, field


@dataclass(slots=True)
class PlanAction:
    priority: 		int
    source: 			str
    action_type: 	str
    payload: 		dict = field(default_factory=dict)
