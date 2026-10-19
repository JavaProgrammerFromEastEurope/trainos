from __future__ import annotations

from .civil_audit_entry import CivilAuditEntry


class CivilAuditRegistry:

    def __init__(self) -> None:
        self._entries: list[CivilAuditEntry] = []

    def register(self, entry: CivilAuditEntry) -> None:
        self._entries.append(entry)

    def entries(self) -> tuple[CivilAuditEntry, ...]:
        return tuple(self._entries)
