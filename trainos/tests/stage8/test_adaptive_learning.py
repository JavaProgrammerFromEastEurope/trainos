from trainos.kernel.learning.adaptive.adaptive_engine import (
    AdaptiveEngine,
)


def test_adaptive_learning():

    engine = AdaptiveEngine()
    result = engine.optimize()

    assert result.success is True
