from trainos.kernel.learning.learning_engine import LearningEngine


def test_learning_core():

    engine = LearningEngine()
    result = engine.train(data=[])

    assert result.improved is True
