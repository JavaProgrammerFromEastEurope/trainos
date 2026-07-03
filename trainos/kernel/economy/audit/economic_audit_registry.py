from __future__ import annotations

from .economic_audit_entry import EconomicAuditEntry


class EconomicAuditRegistry:

    def __init__(self) -> None:
        self._entries: list[EconomicAuditEntry] = []

    def register(
        self,
        entry: EconomicAuditEntry,
    ) -> None:
        self._entries.append(entry)

    def entries(
        self,
    ) -> tuple[EconomicAuditEntry, ...]:
        return tuple(self._entries)
