from __future__ import annotations

from .reasoning_node import ReasoningNode


class DistributedRegistry:

    def __init__(self) -> None:
        self._nodes: list[ReasoningNode] = []

    def register(self, node: ReasoningNode) -> None:
        self._nodes.append(node)

    def nodes(self) -> tuple[ReasoningNode, ...]:
        return tuple(self._nodes)
