from __future__ import annotations

from trainos.kernel.ai.planning.plan import Plan
from .execution_graph import ExecutionGraph
from .execution_node import ExecutionNode


class ExecutionGraphBuilder:
    def build(
        self,
        plan: Plan,
    ) -> ExecutionGraph:
        graph = ExecutionGraph()
        for step in plan.steps:
            graph.add(
                ExecutionNode(
                    id=step.name,
                    payload=step.payload,
                    dependencies=step.depends_on,
                )
            )
        return graph
