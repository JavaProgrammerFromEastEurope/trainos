from __future__ import annotations

from .action_record import (
    ActionRecord,
)


class ActionHistory:

    def __init__(
        self,
    ) -> None:
        self._records: list[ActionRecord] = []

    def add(
        self,
        record: ActionRecord,
    ) -> None:
        self._records.append(
            record,
        )

    def records(
        self,
    ) -> tuple[ActionRecord, ...]:
        return tuple(
            self._records,
        )
