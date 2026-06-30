from __future__ import annotations

from .governance_deliberation import GovernanceDeliberation


class DeliberationRegistry:

    def __init__(self) -> None:
        self._deliberations: list[GovernanceDeliberation] = []

    def register(self, deliberation: GovernanceDeliberation) -> None:
        self._deliberations.append(deliberation)

    def deliberations(self) -> tuple[GovernanceDeliberation, ...]:
        return tuple(self._deliberations)
