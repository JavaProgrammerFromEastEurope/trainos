from __future__ import annotations

from .knowledge_node import KnowledgeNode


class KnowledgeGraph:

    def __init__(self) -> None:
        self._nodes: list[KnowledgeNode] = []

    def add(self, node: KnowledgeNode) -> None:
        self._nodes.append(node)

    def nodes(self) -> tuple[KnowledgeNode, ...]:
        return tuple(self._nodes)
