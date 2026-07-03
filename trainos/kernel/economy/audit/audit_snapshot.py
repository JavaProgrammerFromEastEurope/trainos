from dataclasses import dataclass


@dataclass(frozen=True)
class AuditSnapshot:

    total_entries: int