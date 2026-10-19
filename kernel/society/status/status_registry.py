from __future__ import annotations

from .civil_status import CivilStatus


class StatusRegistry:

    def __init__(self) -> None:
        self._statuses: dict[str, CivilStatus] = {}

    def register(self, status: CivilStatus) -> None:
        self._statuses[status.entity_id] = status

    def get(self, entity_id: str) -> CivilStatus | None:
        return self._statuses.get(entity_id)
