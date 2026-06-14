from trainos.kernel.world.simulation.simulation_engine import SimulationEngine


def test_simulation():

    engine = SimulationEngine()

    assert engine._runtime.tick.value == 0
    assert engine._runtime.clock.time == 0.0

    engine.tick(1.0)

    assert engine._runtime.tick.value == 1
    assert engine._runtime.clock.time == 1.0

    engine.tick(0.5)

    assert engine._runtime.tick.value == 2
    assert engine._runtime.clock.time == 1.5
