from dataclasses import dataclass


@dataclass(frozen=True)
class JustificationPolicy:

    require_explanation: bool