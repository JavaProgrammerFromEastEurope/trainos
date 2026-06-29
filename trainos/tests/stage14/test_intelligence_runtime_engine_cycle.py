from trainos.kernel.intelligence.runtime.intelligence_runtime_engine import (
    IntelligenceRuntimeEngine,
)


def test_intelligence_runtime_engine_cycle():

    engine = IntelligenceRuntimeEngine()

    cycle_1 = engine.next_cycle()
    cycle_2 = engine.next_cycle()

    assert cycle_1.index == 1
    assert cycle_2.index == 2
