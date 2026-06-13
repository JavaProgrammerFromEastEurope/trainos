from trainos.kernel.ai.reasoning.reasoning_context import (
    ReasoningContext,
)

from trainos.kernel.ai.reasoning.reasoning_engine import (
    ReasoningEngine,
)

from trainos.kernel.ai.reasoning.rule import Rule


def test_reasoning_engine():
    engine = ReasoningEngine()
    engine.rules.add(Rule(name="r1", condition="enemy", conclusion="attack"))
    result = engine.reason(ReasoningContext(state={"enemy": True}))
    assert result.success is True
    assert result.conclusion == "attack"
