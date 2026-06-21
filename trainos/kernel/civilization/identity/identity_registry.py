from __future__ import annotations

from .identity import Identity


class IdentityRegistry:

    def __init__(self) -> None:
        self._identities: list[Identity] = []

    def add(self, identity: Identity) -> None:
        self._identities.append(identity)

    def identities(self) -> tuple[Identity, ...]:
        return tuple(self._identities)
