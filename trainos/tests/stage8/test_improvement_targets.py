from trainos.kernel.learning.improvement.adaptation_engine import (
    AdaptationEngine,
)


def test_improvement_targets():

    engine = AdaptationEngine()

    target = engine.adapt()

    assert target.name == "navigation"
