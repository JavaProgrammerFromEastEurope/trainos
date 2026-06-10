# kernel/config/config_service.py

from __future__ import annotations

from trainos.kernel.config.config_repository import ConfigRepository
from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState


class ConfigService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="config",
            startup_priority=5,
            dependencies=(),
        )
        self._repository = ConfigRepository()

    @property
    def repository(self) -> ConfigRepository:
        return self._repository

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:
        pass

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:

        self._repository.clear()

    def health_check(self) -> bool:
        return not self.failed

    def get(
        self,
        key: str,
        default: object | None = None,
    ) -> object | None:
        return self._repository.get(key, default)

    def set(
        self,
        key: str,
        value: object,
    ) -> None:
        self._repository.set(key, value)
