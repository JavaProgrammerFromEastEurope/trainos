from trainos.kernel.learning.self_evaluation.evaluation_engine import (
    EvaluationEngine,
)


def test_self_evaluation():

    engine = EvaluationEngine()

    result = engine.run()

    assert result.success is True
