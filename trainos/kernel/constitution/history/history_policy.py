from dataclasses import dataclass


@dataclass(frozen=True)
class HistoryPolicy:

    preserve_all_versions: bool