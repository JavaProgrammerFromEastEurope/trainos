from trainos.kernel.ai.execution_graph.execution_graph_builder import (
    ExecutionGraphBuilder,
)

from trainos.kernel.ai.planning.plan import Plan
from trainos.kernel.ai.planning.plan_step import PlanStep


def test_execution_graph():
    plan = Plan()
    plan.add(PlanStep(name="A", payload={}, depends_on=[]))
    graph = ExecutionGraphBuilder().build(plan)
    assert len(graph.all_nodes()) == 1
