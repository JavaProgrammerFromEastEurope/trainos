from dataclasses import dataclass


@dataclass
class LinkingPolicy:
    allow_cycles: bool