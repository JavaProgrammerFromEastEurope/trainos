from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceUnit:

    unit_id: 	str
    name: 		str
    symbol: 	str