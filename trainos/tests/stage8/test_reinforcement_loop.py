from trainos.kernel.learning.reinforcement.reinforcement_engine import (
    ReinforcementEngine,
)


def test_reinforcement_loop():

    engine = ReinforcementEngine()
    result = engine.train()

    assert result.improved is True
