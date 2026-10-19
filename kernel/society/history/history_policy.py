from dataclasses import dataclass


@dataclass(frozen=True)
class HistoryPolicy:

    immutable_history: bool
    chronological_order: bool