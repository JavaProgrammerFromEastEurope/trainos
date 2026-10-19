from __future__ import annotations

from .cognition_snapshot import CognitionSnapshot


class CognitionRegistry:

    def __init__(self) -> None:
        self._snapshots: list[CognitionSnapshot] = []

    def register(self, snapshot: CognitionSnapshot) -> None:
        self._snapshots.append(snapshot)

    def snapshots(self) -> tuple[CognitionSnapshot, ...]:
        return tuple(self._snapshots)
