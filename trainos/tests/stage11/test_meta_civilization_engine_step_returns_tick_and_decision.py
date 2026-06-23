from trainos.kernel.metacivilization.engine.meta_civilization_engine import MetaCivilizationEngine
from trainos.kernel.metacivilization.engine.meta_state import MetaState


def test_meta_civilization_engine_step_returns_tick_and_decision():

    engine 	= MetaCivilizationEngine()
    state 	= MetaState()
    result 	= engine.step(state)

    assert "tick" in result
    assert "decision" in result