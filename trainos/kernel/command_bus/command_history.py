from __future__ import annotations

from typing import List
from .command_record import CommandRecord


class CommandHistory:

    def __init__(self) -> None:
        self._records: List[CommandRecord] = []

    def append(
        self,
        record: CommandRecord,
    ) -> None:
        self._records.append(record)

    def all(self) -> list[CommandRecord]:
        return list(self._records)

    def clear(self) -> None:
        self._records.clear()

    def last(self) -> CommandRecord | None:
        if not self._records:
            return None
        return self._records[-1]
