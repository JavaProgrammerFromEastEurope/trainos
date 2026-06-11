# tests/stage2/test_clock_service.py

from trainos.kernel.clock.clock_service import ClockService
from trainos.kernel.lifecycle.kernel_service import ServiceState


def test_clock_service():

    clock = ClockService()

    clock.initialize()
    clock.start()

    clock.update(0.1)
    clock.update(0.2)

    assert clock.state == ServiceState.RUNNING
    assert clock.tick_count == 2
    assert abs(clock.uptime_seconds - 0.3) < 1e-6
    assert clock.delta_time == 0.2
