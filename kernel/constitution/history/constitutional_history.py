from dataclasses import dataclass

from .history_entry import ConstitutionalHistoryEntry


@dataclass(frozen=True)
class ConstitutionalHistory:

    entries: tuple[
        ConstitutionalHistoryEntry,
        ...
    ]