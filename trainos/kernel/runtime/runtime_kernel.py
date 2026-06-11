# kernel/runtime/runtime_kernel.py

from __future__ import annotations

from trainos.kernel.clock.clock_service import ClockService
from trainos.kernel.health.health_monitor_service import HealthMonitorService
from trainos.kernel.kernel import Kernel
from trainos.kernel.runtime.runtime_controller_service import RuntimeControllerService
from trainos.kernel.runtime.runtime_metrics_service import RuntimeMetricsService
from trainos.kernel.runtime.runtime_snapshot import RuntimeSnapshot
from trainos.kernel.scheduler.scheduler_service import SchedulerService
from trainos.kernel.time.time_service import TimeService


class RuntimeKernel(Kernel):

    def __init__(self) -> None:
        super().__init__()

        self._clock_service 			= ClockService()
        self._time_service 				= TimeService()
        self._scheduler_service 	= SchedulerService()
        self._runtime_controller 	= RuntimeControllerService()
        self._runtime_metrics 		= RuntimeMetricsService()
        self._health_monitor 			= HealthMonitorService()

        self.register_service(self._clock_service)
        self.register_service(self._time_service)
        self.register_service(self._scheduler_service)
        self.register_service(self._runtime_controller)
        self.register_service(self._runtime_metrics)
        self.register_service(self._health_monitor)

        for service in self._services.values():
            self._health_monitor.register_service(service)

    @property
    def clock(self) -> ClockService:
        return self._clock_service

    @property
    def time(self) -> TimeService:
        return self._time_service

    @property
    def scheduler(self) -> SchedulerService:
        return self._scheduler_service

    @property
    def runtime_controller(self) -> RuntimeControllerService:
        return self._runtime_controller

    @property
    def metrics(self) -> RuntimeMetricsService:
        return self._runtime_metrics

    @property
    def health(self) -> HealthMonitorService:
        return self._health_monitor

    @property
    def snapshot(self) -> RuntimeSnapshot:
        return RuntimeSnapshot(
            state 	= self._runtime_controller.runtime_state,
            metrics = self._runtime_metrics.metrics,
            health 	=	self._health_monitor.health_check(),
        )

    def update(self, dt: float) -> None:
        super().update(dt)
        self._runtime_metrics.set_active_services(len(self._services))
