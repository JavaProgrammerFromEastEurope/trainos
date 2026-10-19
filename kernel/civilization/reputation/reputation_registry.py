from __future__ import annotations

from .reputation import (
    Reputation,
)


class ReputationRegistry:

    def __init__(self) -> None:
        self._reputations: list[Reputation] = []

    def add(self, reputation: Reputation) -> None:
        self._reputations.append(reputation)

    def reputations(self) -> tuple[Reputation, ...]:
        return tuple(self._reputations)
