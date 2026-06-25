from trainos.kernel.evolution.cultural_runtime.cultural_runtime_engine import CulturalRuntimeEngine


def test_cultural_runtime_engine_step():

    engine = CulturalRuntimeEngine()

    tick_1 = engine.step()
    tick_2 = engine.step()

    assert tick_1.index == 1
    assert tick_2.index == 2