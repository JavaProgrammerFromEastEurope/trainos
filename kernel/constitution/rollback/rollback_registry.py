from __future__ import annotations

from .constitutional_rollback import ConstitutionalRollback


class RollbackRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalRollback] = []

    def register(
        self,
        rollback: ConstitutionalRollback,
    ) -> None:
        self._entries.append(rollback)

    def entries(
        self,
    ) -> tuple[ConstitutionalRollback, ...]:
        return tuple(self._entries)
