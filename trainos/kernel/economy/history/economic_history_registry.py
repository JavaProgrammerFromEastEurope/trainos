from __future__ import annotations

from .economic_history_entry import EconomicHistoryEntry


class EconomicHistoryRegistry:

    def __init__(self) -> None:
        self._entries: list[EconomicHistoryEntry] = []

    def register(
        self,
        entry: EconomicHistoryEntry,
    ) -> None:
        self._entries.append(entry)

    def entries(
        self,
    ) -> tuple[EconomicHistoryEntry, ...]:
        return tuple(self._entries)
