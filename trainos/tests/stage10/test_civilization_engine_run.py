from trainos.kernel.civilization.civilization.civilization_engine import (
    CivilizationEngine,
)
from trainos.kernel.civilization.civilization.civilization_state import (
    CivilizationState,
)


def test_civilization_engine_run():

    engine = CivilizationEngine()
    civilization = engine.run()

    assert civilization.state == CivilizationState.STABLE
