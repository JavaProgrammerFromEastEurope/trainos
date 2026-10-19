from __future__ import annotations

from .knowledge_snapshot import KnowledgeSnapshot


class KnowledgeHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[KnowledgeSnapshot] = []

    def add(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> None:
        self._history.append(snapshot)

    def snapshots(
        self,
    ) -> tuple[KnowledgeSnapshot, ...]:
        return tuple(self._history)
