from __future__ import annotations

from typing import Dict
from .memory_record import MemoryRecord


class LongTermMemory:

    def __init__(self) -> None:
        self._records: Dict[
            str,
            MemoryRecord,
        ] = {}

    def store(
        self,
        record: MemoryRecord,
    ) -> None:
        self._records[record.key] = record

    def recall(
        self,
        key: str,
    ) -> MemoryRecord | None:
        return self._records.get(
            key,
        )
