from dataclasses import dataclass


@dataclass(frozen=True)
class IntegrationPolicy:

    require_ratification: bool
    preserve_history: bool