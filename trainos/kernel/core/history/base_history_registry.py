from __future__ import annotations

from typing import Generic, TypeVar

from .base_history_entry import BaseHistoryEntry

T = TypeVar("T")


class BaseHistoryRegistry(Generic[T]):

    def __init__(self) -> None:
        self._history: list[BaseHistoryEntry] = []

    def record(self, entry: BaseHistoryEntry) -> None:
        self._history.append(entry)

    def all(self) -> tuple[BaseHistoryEntry, ...]:
        return tuple(self._history)

    def latest(self) -> BaseHistoryEntry | None:
        if not self._history:
            return None
        return self._history[-1]
