from kernel.simulation.clock.simulation_clock import SimulationClock
from kernel.simulation.clock.clock_engine 		import ClockEngine
from kernel.simulation.clock.clock_status 		import ClockStatus


def test_simulation_clock():

    engine = ClockEngine()
    clock = SimulationClock(
        clock_id="CLOCK1",
        tick=0,
        status=ClockStatus.STOPPED,
    )
    started = engine.start(clock)
    assert started.status == ClockStatus.RUNNING

    advanced = engine.advance(started)
    assert advanced.tick == 1
