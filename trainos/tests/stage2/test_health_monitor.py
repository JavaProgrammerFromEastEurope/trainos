# tests/stage2/test_health_monitor.py

from trainos.kernel.health.health_monitor_service import HealthMonitorService
from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState


class DummyService(KernelService):

    def __init__(self):
        super().__init__(
            name="dummy",
        )

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)


def test_health_monitor():

    monitor = HealthMonitorService()

    service = DummyService()

    monitor.register_service(service)

    report = monitor.health_check()

    assert report.healthy is True
    assert report.checked_services == 1
    assert report.failed_services == 0
    assert report.failed_service_names == ()

    service._mark_failed("failure")

    report = monitor.health_check()

    assert report.healthy is False
    assert report.failed_services == 1
    assert report.failed_service_names == ("dummy",)
