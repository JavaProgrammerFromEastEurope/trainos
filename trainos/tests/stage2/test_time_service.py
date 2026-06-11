# tests/stage2/test_time_service.py

from trainos.kernel.time.time_service import TimeService
from trainos.kernel.lifecycle.kernel_service import ServiceState


def test_time_service():

    service = TimeService()

    service.initialize()
    service.start()

    service.update(0.5)
    service.update(1.0)

    assert service.state == ServiceState.RUNNING
    assert service.tick_count == 2
    assert abs(service.elapsed_seconds - 1.5) < 1e-6

    snapshot = service.simulation_time

    assert snapshot.tick_count == 2
    assert abs(snapshot.elapsed_seconds - 1.5) < 1e-6

    service.reset()

    assert service.tick_count == 0
    assert service.elapsed_seconds == 0.0
