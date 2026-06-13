from __future__ import annotations

from trainos.kernel.state.state_history_record import (
    StateHistoryRecord,
)


class StateHistory:

    def __init__(self) -> None:
        self._records: list[StateHistoryRecord] = []

    def append(
        self,
        record: StateHistoryRecord,
    ) -> None:
        self._records.append(
            record,
        )

    def clear(self) -> None:
        self._records.clear()

    @property
    def records(
        self,
    ) -> tuple[
        StateHistoryRecord,
        ...,
    ]:
        return tuple(
            self._records,
        )

    @property
    def size(
        self,
    ) -> int:
        return len(
            self._records,
        )

    def latest(
        self,
    ) -> StateHistoryRecord | None:
        if not self._records:
            return None
        return self._records[-1]
