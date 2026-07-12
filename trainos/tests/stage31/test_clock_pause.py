from kernel.simulation.clock.simulation_clock import SimulationClock
from kernel.simulation.clock.clock_engine 		import ClockEngine
from kernel.simulation.clock.clock_status 		import ClockStatus


def test_clock_pause():

    engine = ClockEngine()
    clock = SimulationClock(
        clock_id="CLOCK1",
        tick=10,
        status=ClockStatus.RUNNING,
    )
    paused = engine.pause(clock)

    assert paused.status == ClockStatus.PAUSED
    assert paused.tick == 10
