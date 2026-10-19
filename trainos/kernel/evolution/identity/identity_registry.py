from __future__ import annotations

from .identity_snapshot import IdentitySnapshot


class IdentityRegistry:

    def __init__(self) -> None:
        self._snapshots: list[IdentitySnapshot] = []

    def register(self, snapshot: IdentitySnapshot) -> None:
        self._snapshots.append(snapshot)

    def snapshots(self) -> tuple[IdentitySnapshot, ...]:
        return tuple(self._snapshots)
