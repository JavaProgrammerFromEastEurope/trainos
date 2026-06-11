# tests/stage2/test_runtime_metrics.py

from trainos.kernel.runtime.runtime_metrics_service import RuntimeMetricsService
from trainos.kernel.lifecycle.kernel_service import ServiceState


def test_runtime_metrics():

    metrics = RuntimeMetricsService()

    metrics.initialize()
    metrics.start()

    metrics.update(0.1)
    metrics.update(0.1)

    metrics.set_active_services(5)

    snapshot = metrics.snapshot

    assert metrics.state == ServiceState.RUNNING

    assert snapshot.metrics.tick_count == 2
    assert abs(snapshot.metrics.uptime_seconds - 0.2) < 1e-6
    assert snapshot.metrics.active_services == 5

    # FPS = ticks / time → 2 / 0.2 = 10
    assert abs(snapshot.metrics.fps - 10.0) < 1e-6
