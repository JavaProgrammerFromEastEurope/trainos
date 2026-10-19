from dataclasses import dataclass


@dataclass(frozen=True)
class BaseLifecycle:

    entity_id: 	str
    state: 			str