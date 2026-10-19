from __future__ import annotations

from .institution_history_entry import InstitutionHistoryEntry


class InstitutionHistoryRegistry:

    def __init__(self) -> None:
        self._history: dict[
            str,
            tuple[InstitutionHistoryEntry, ...],
        ] = {}

    def register(
        self,
        entry: InstitutionHistoryEntry,
    ) -> None:
        current = self._history.get(entry.institution_id, ())
        self._history[entry.institution_id] = current + (entry,)

    def history(
        self,
        institution_id: str,
    ) -> tuple[InstitutionHistoryEntry, ...]:
        return self._history.get(institution_id, ())
