from trainos.kernel.behavior.cognition.cognitive_engine import (
    CognitiveEngine,
)


def test_cognitive_layer():

    engine = CognitiveEngine()
    result = engine.step()

    assert result.success is True
