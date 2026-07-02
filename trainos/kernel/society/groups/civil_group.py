from dataclasses import dataclass


@dataclass(frozen=True)
class CivilGroup:

    group_id: str
    name: 		str