from dataclasses import dataclass


@dataclass(frozen=True)
class RollbackPolicy:

    preserve_history: bool
    allow_immutable_restore: bool