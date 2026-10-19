from dataclasses import dataclass


@dataclass(frozen=True)
class StatusDefinition:

    status_id: 		str
    name: 				str
    description: 	str