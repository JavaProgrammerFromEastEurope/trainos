from dataclasses import dataclass


@dataclass
class GOAPAction:

    name: str
    cost: float = 1.0
