from __future__ import annotations

from .task_node import (
    TaskNode,
)


class TaskGraph:

    def __init__(
        self,
    ) -> None:
        self._nodes: list[TaskNode] = []

    def add(
        self,
        node: TaskNode,
    ) -> None:
        self._nodes.append(
            node,
        )

    def nodes(
        self,
    ) -> tuple[TaskNode, ...]:
        return tuple(self._nodes)
