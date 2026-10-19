from __future__ import annotations

from .institution_audit_entry import InstitutionAuditEntry


class InstitutionAuditRegistry:

    def __init__(self) -> None:
        self._entries: list[InstitutionAuditEntry] = []

    def register(self, entry: InstitutionAuditEntry) -> None:
        self._entries.append(entry)

    def entries(self) -> tuple[InstitutionAuditEntry, ...]:
        return tuple(self._entries)
