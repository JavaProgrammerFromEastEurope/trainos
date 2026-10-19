from dataclasses import dataclass


@dataclass(frozen=True)
class ConstitutionalHistoryEntry:

    version: str
    amendment_id: str