from __future__ import annotations

from .memory_record import MemoryRecord


class EpisodicMemory:

    def __init__(self) -> None:
        self._episodes: list[MemoryRecord] = []

    def remember(
        self,
        record: MemoryRecord,
    ) -> None:
        self._episodes.append(
            record,
        )

    def episodes(
        self,
    ) -> list[MemoryRecord]:
        return self._episodes
