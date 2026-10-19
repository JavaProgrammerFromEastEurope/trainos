from __future__ import annotations

from .audit_entry import ConstitutionalAuditEntry


class AuditRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalAuditEntry] = []

    def register(
        self,
        entry: ConstitutionalAuditEntry,
    ) -> None:
        self._entries.append(entry)

    def entries(
        self,
    ) -> tuple[ConstitutionalAuditEntry, ...]:
        return tuple(self._entries)
