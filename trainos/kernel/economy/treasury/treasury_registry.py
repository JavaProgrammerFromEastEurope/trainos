from __future__ import annotations

from .treasury import Treasury


class TreasuryRegistry:

    def __init__(self) -> None:
        self._treasuries: dict[str, Treasury] = {}

    def register(
        self,
        treasury: Treasury,
    ) -> None:
        self._treasuries[treasury.treasury_id] = treasury

    def get(
        self,
        treasury_id: str,
    ) -> Treasury | None:
        return self._treasuries.get(treasury_id)

    def all(
        self,
    ) -> tuple[Treasury, ...]:
        return tuple(self._treasuries.values())
