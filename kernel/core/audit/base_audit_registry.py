from __future__ import annotations

from typing import Generic, TypeVar

from .base_audit_entry import BaseAuditEntry

T = TypeVar("T")


class BaseAuditRegistry(Generic[T]):

    def __init__(self) -> None:
        self._events: list[BaseAuditEntry] = []

    def record(self, entry: BaseAuditEntry) -> None:
        self._events.append(entry)

    def all(self) -> tuple[BaseAuditEntry, ...]:
        return tuple(self._events)

    def filter_by_actor(self, actor_id: str):
        return tuple(e for e in self._events if e.event.actor_id == actor_id)
