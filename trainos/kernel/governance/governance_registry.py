from __future__ import annotations

from .authority import GovernanceAuthority


class GovernanceRegistry:

    def __init__(self) -> None:
        self._authorities: list[GovernanceAuthority] = []

    def register(self, authority: GovernanceAuthority) -> None:
        self._authorities.append(authority)

    def authorities(self) -> tuple[GovernanceAuthority, ...]:
        return tuple(self._authorities)
