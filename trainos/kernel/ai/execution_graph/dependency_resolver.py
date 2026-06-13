from __future__ import annotations

from .execution_graph import (
    ExecutionGraph,
)


class DependencyResolver:

    def ready_nodes(
        self,
        graph: ExecutionGraph,
        completed: set[str],
    ) -> list[str]:
        result: list[str] = []
        for node in graph.all_nodes():
            if node.id in completed:
                continue
            if all(
                dependency in completed
                for dependency in node.dependencies
            ):
                result.append(node.id)
        return result