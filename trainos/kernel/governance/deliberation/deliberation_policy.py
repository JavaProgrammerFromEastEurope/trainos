from dataclasses import dataclass


@dataclass(frozen=True)
class DeliberationPolicy:

    require_consensus: bool