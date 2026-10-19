"""Compatibility exports for constitutional audit records.

The canonical record model lives in ``audit_entry`` so the audit engine,
registry, and public imports share one type rather than duplicate dataclasses.
"""

from .audit_entry import ConstitutionalAuditEntry

ConstitutionalAudit = ConstitutionalAuditEntry

__all__ = ["ConstitutionalAudit", "ConstitutionalAuditEntry"]
