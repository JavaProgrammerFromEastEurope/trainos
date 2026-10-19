from __future__ import annotations

from .skill_record import (
    SkillRecord,
)


class SkillHistory:

    def __init__(
        self,
    ) -> None:
        self._records: list[SkillRecord] = []

    def add(
        self,
        record: SkillRecord,
    ) -> None:
        self._records.append(record)

    def records(
        self,
    ) -> tuple[SkillRecord, ...]:
        return tuple(self._records)
