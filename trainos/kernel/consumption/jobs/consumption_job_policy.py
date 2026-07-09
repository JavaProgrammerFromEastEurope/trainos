from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionJobPolicy:

    require_request: 	bool = True
    require_policy: 	bool = True
    require_consumer: bool = True