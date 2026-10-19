from kernel.learning.improvement.adaptation_engine import (
    AdaptationEngine,
)
from kernel.learning.self_evaluation.improvement_engine import (
    ImprovementEngine as SelfEvaluationImprovementEngine,
)


def test_improvement_targets():

    engine = AdaptationEngine()

    target = engine.adapt()

    assert target.name == "navigation"

    self_evaluation_target = SelfEvaluationImprovementEngine().target()
    assert self_evaluation_target.name == "navigation"
