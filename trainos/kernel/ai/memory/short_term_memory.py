from __future__ import annotations

from collections import deque

from .memory_record import MemoryRecord


class ShortTermMemory:

    def __init__(
        self,
        capacity: int = 100,
    ) -> None:
        self._records = deque(
            maxlen=capacity,
        )

    def add(
        self,
        record: MemoryRecord,
    ) -> None:
        self._records.append(
            record,
        )

    def all(
        self,
    ) -> list[MemoryRecord]:
        return list(
            self._records,
        )
