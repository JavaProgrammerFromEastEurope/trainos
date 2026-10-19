from __future__ import annotations

from .audit_entry import ConstitutionalAuditEntry


class AuditEngine:
    """Records an already-validated constitutional audit entry."""

    def record(self, audit: ConstitutionalAuditEntry) -> ConstitutionalAuditEntry:
        if not isinstance(audit, ConstitutionalAuditEntry):
            raise TypeError("audit must be a ConstitutionalAuditEntry")
        return audit
