from dataclasses import dataclass


@dataclass(frozen=True)
class Reserve:

    reserve_id: 		str
    treasury_id: 		str
    description: 		str