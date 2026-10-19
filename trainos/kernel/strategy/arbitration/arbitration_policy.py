from dataclasses import dataclass


@dataclass(frozen=True)
class ArbitrationPolicy:

    prefer_high_priority: bool