from trainos.kernel.metacivilization.engine.meta_civilization_engine import MetaCivilizationEngine
from trainos.kernel.metacivilization.engine.meta_state import MetaState


def test_meta_civilization_engine_tick_increases():

    engine = MetaCivilizationEngine()

    state = MetaState()

    r1 = engine.step(state)
    r2 = engine.step(state)

    assert r2["tick"] == r1["tick"] + 1