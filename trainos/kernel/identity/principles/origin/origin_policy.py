from dataclasses import dataclass


@dataclass(frozen=True)
class OriginPolicy:

    preserve_history: bool