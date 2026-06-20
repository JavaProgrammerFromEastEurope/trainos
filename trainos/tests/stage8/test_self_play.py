from trainos.kernel.learning.self_play.self_play_engine import SelfPlayEngine


def test_self_play():

    engine = SelfPlayEngine()
    result = engine.run()

    assert result.success is True
