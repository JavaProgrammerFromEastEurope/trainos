from __future__ import annotations

from typing import Dict

from .execution_node import ExecutionNode


class ExecutionGraph:

    def __init__(self) -> None:
        self._nodes: Dict[
            str,
            ExecutionNode,
        ] = {}

    def add(
        self,
        node: ExecutionNode,
    ) -> None:
        self._nodes[node.id] = node

    def get(
        self,
        node_id: str,
    ) -> ExecutionNode:
        return self._nodes[node_id]

    def all_nodes(
        self,
    ) -> list[ExecutionNode]:
        return list(self._nodes.values())
