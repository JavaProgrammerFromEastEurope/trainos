from trainos.kernel.metacivilization.recursive_runtime.recursive_runtime_engine import RecursiveRuntimeEngine


def test_recursive_runtime_engine_tick_increases():

    engine = RecursiveRuntimeEngine()
    tick_1 = engine.step()
    tick_2 = engine.step()

    assert tick_2.index == tick_1.index + 1