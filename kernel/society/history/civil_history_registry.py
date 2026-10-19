from __future__ import annotations

from .civil_history_entry import CivilHistoryEntry


class CivilHistoryRegistry:

    def __init__(self) -> None:
        self._history: dict[str, tuple[CivilHistoryEntry, ...]] = {}

    def register(self, entry: CivilHistoryEntry) -> None:
        current = self._history.get(entry.entity_id, ())
        self._history[entry.entity_id] = current + (entry,)

    def history(self, entity_id: str) -> tuple[CivilHistoryEntry, ...]:
        return self._history.get(entity_id, ())
