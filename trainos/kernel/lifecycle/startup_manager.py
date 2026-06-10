# kernel/lifecycle/startup_manager.py

from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter
from trainos.kernel.lifecycle.kernel_service import KernelService


@dataclass(slots=True)
class StartupManagerStatus:
    registered_services: int
    running_services: int
    failed_services: int
    boot_completed: bool
    boot_time_seconds: float


class StartupManager:

    def __init__(self) -> None:

        self._services: dict[str, KernelService] = {}
        self._startup_order: list[KernelService] = []
        self._running = False
        self._initialized = False
        self._boot_completed = False
        self._boot_time_seconds = 0.0

    def register(self, service: KernelService) -> None:

        if service.name in self._services:
            raise ValueError(f"Service '{service.name}' already registered.")
        self._services[service.name] = service

    def get_service(self, name: str) -> KernelService:
        if name not in self._services:
            raise KeyError(name)

        return self._services[name]

    def initialize_all(self) -> None:
        self._startup_order = self._resolve_startup_order()
        for service in self._startup_order:
            service.initialize()
        self._initialized = True

    def start_all(self) -> None:
        if not self._initialized:
            self.initialize_all()
        started_at = perf_counter()
        for service in self._startup_order:
            service.start()
        self._boot_time_seconds = perf_counter() - started_at
        self._running = True
        self._boot_completed = True

    def stop_all(self) -> None:
        for service in reversed(self._startup_order):
            service.stop()
        self._running = False

    def dispose_all(self) -> None:

        for service in reversed(self._startup_order):
            service.dispose()

    def restart_service(self, name: str) -> None:
        service = self.get_service(name)
        service.stop()
        service.dispose()
        service.initialize()
        service.start()

    def health_check(self) -> dict[str, bool]:
        return {
            service.name: service.health_check() for service in self._services.values()
        }

    def status(self) -> StartupManagerStatus:
        running_services = sum(
            1 for service in self._services.values() if service.health_check()
        )

        failed_services = sum(
            1 for service in self._services.values() if service.failed
        )

        return StartupManagerStatus(
            registered_services=len(self._services),
            running_services=running_services,
            failed_services=failed_services,
            boot_completed=self._boot_completed,
            boot_time_seconds=self._boot_time_seconds,
        )

    def _resolve_startup_order(self) -> list[KernelService]:
        visited: set[str] = set()
        temporary: set[str] = set()
        result: list[KernelService] = []

        def visit(service_name: str) -> None:

            if service_name in temporary:
                raise RuntimeError(f"Circular dependency detected: {service_name}")

            if service_name in visited:
                return

            temporary.add(service_name)

            service = self._services[service_name]

            for dependency in service.dependencies:

                if dependency not in self._services:
                    raise RuntimeError(f"Dependency '{dependency}' not registered.")

                visit(dependency)

            temporary.remove(service_name)

            visited.add(service_name)

            result.append(service)

        ordered_names = sorted(
            self._services.keys(),
            key=lambda x: self._services[x].startup_priority,
        )

        for name in ordered_names:
            visit(name)

        return result
