# tests/stage2/test_runtime_kernel_integration.py

from trainos.kernel.runtime.runtime_bootstrap import create_runtime_kernel


def test_runtime_kernel_integration():

    kernel = create_runtime_kernel()

    kernel.update(0.1)
    kernel.update(0.1)

    snapshot = kernel.snapshot

    assert snapshot.metrics.tick_count == 2
    assert snapshot.metrics.active_services == 6
    assert snapshot.health.healthy is True
    assert kernel.runtime_controller.is_running is True