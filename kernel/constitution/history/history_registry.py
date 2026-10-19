from __future__ import annotations

from .history_entry import ConstitutionalHistoryEntry


class HistoryRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalHistoryEntry] = []

    def register(
        self,
        entry: ConstitutionalHistoryEntry,
    ) -> None:
        self._entries.append(entry)

    def entries(
        self,
    ) -> tuple[ConstitutionalHistoryEntry, ...]:
        return tuple(self._entries)
