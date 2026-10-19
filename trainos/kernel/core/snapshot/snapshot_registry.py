from __future__ import annotations

from typing import Generic, TypeVar

from .base_snapshot import BaseSnapshot

T = TypeVar("T")


class SnapshotRegistry(Generic[T]):

    def __init__(self) -> None:
        self._snapshots: list[BaseSnapshot[T]] = []

    def register(self, snapshot: BaseSnapshot[T]) -> None:
        self._snapshots.append(snapshot)

    def latest(self) -> BaseSnapshot[T] | None:
        if not self._snapshots:
            return None
        return self._snapshots[-1]

    def all(self) -> tuple[BaseSnapshot[T], ...]:
        return tuple(self._snapshots)
