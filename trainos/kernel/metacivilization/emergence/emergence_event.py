from dataclasses import dataclass


@dataclass
class EmergenceEvent:

    source: 	str
    pattern:	str
    strength: float