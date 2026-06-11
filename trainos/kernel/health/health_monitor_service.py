# kernel/health/health_monitor_service.py

from __future__ import annotations

from trainos.kernel.health.health_report import HealthReport
from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)


class HealthMonitorService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="health_monitor",
            dependencies=(),
        )

        self._services: dict[str, KernelService] = {}

    # ---------------- lifecycle ----------------

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._services.clear()

    def update(self, dt: float) -> None:
        return

    # ---------------- registry ----------------

    def register_service(self, service: KernelService) -> None:

        # ❗ avoid self-registration (CRITICAL FIX)
        if service is self:
            return

        self._services[service.name] = service

    def unregister_service(self, service: KernelService) -> None:

        self._services.pop(service.name, None)

    # ---------------- health logic ----------------

    def health_check(self) -> HealthReport:

        failed_services: list[str] = []

        # IMPORTANT: only use local registry, NOT kernel.services
        for service in self._services.values():

            # safety guard
            if service is self:
                continue

            try:
                if not service.health_check():
                    failed_services.append(service.name)

            except Exception:
                failed_services.append(service.name)

        return HealthReport(
            healthy=len(failed_services) == 0,
            checked_services=len(self._services),
            failed_services=len(failed_services),
            failed_service_names=tuple(failed_services),
        )
