from dataclasses import dataclass


@dataclass(frozen=True)
class AuditPolicy:

    immutable_log: bool
    preserve_full_trace: bool