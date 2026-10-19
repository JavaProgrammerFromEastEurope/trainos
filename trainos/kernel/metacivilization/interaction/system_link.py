from dataclasses import dataclass


@dataclass
class SystemLink:

    source: str
    target: str
    weight: float