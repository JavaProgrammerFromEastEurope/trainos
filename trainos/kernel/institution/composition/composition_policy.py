from dataclasses import dataclass


@dataclass(frozen=True)
class CompositionPolicy:

    prevent_cycles: bool
    allow_multiple_components: bool