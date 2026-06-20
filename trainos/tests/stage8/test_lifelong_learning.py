from trainos.kernel.learning.lifelong.lifelong_engine import LifelongEngine


def test_lifelong_learning():

    engine = LifelongEngine()
    result = engine.run()

    assert result.success is True
