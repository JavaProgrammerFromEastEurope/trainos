from dataclasses import dataclass


@dataclass(frozen=True)
class AdaptationPolicy:

    allow_replanning: bool