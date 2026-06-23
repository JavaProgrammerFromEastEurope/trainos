from dataclasses import dataclass


@dataclass
class EvolutionRule:

    pattern: str
    allowed: bool