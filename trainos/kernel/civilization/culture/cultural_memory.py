from __future__ import annotations

from .cultural_record import CulturalRecord


class CulturalMemory:

    def __init__(self) -> None:
        self._records: list[CulturalRecord] = []

    def add(self, record: CulturalRecord) -> None:
        self._records.append(record)

    def records(self) -> tuple[CulturalRecord, ...]:
        return tuple(self._records)
