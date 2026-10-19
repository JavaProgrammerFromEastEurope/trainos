from __future__ import annotations

from .historical_record import HistoricalRecord


class HistoryRegistry:

    def __init__(self) -> None:
        self._records: list[HistoricalRecord] = []

    def add(self, record: HistoricalRecord) -> None:
        self._records.append(record)

    def records(self) -> tuple[HistoricalRecord, ...]:
        return tuple(self._records)
