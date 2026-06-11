from trainos.kernel.lifecycle.kernel_service import KernelService, ServiceState
from trainos.kernel.runtime.runtime_snapshot import RuntimeSnapshot
from trainos.kernel.runtime.runtime_metrics import RuntimeMetrics


class RuntimeMetricsService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="runtime_metrics",
            dependencies=(),
        )

        self.metrics = RuntimeMetrics()
        self._health = True

    # ---------------- lifecycle ----------------

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)

    # ---------------- runtime update ----------------

    def update(self, dt: float) -> None:

        self.metrics.tick_count += 1
        self.metrics.uptime_seconds += dt

    def set_active_services(self, count: int) -> None:
        self.metrics.active_services = count

    # ---------------- snapshot (CRITICAL PART) ----------------

    @property
    def snapshot(self) -> RuntimeSnapshot:

        return RuntimeSnapshot(
            state 	= self.state,
            metrics = self.metrics,
            health	= self._health,
        )
