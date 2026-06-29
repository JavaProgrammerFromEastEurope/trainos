from trainos.kernel.intelligence.reasoning.reasoning_registry import ReasoningRegistry
from trainos.kernel.intelligence.reasoning.reasoning_result import ReasoningResult


def test_reasoning_registry_register():

    registry = ReasoningRegistry()
    result = ReasoningResult(
        conclusion="repair water recycler",
    )
    registry.register(result)
    assert registry.results() == (result,)
