from dataclasses import dataclass


@dataclass(frozen=True)
class ConflictPolicy:

    prioritize_survival: 			bool
    allow_dynamic_reordering: bool
