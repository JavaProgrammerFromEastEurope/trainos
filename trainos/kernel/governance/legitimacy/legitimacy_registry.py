from __future__ import annotations

from .governance_legitimacy import GovernanceLegitimacy


class LegitimacyRegistry:

    def __init__(self) -> None:
        self._records: list[GovernanceLegitimacy] = []

    def register(self, legitimacy: GovernanceLegitimacy) -> None:
        self._records.append(legitimacy)

    def records(self) -> tuple[GovernanceLegitimacy, ...]:
        return tuple(self._records)
