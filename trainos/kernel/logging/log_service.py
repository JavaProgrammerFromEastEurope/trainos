# kernel/logging/log_service.py

from __future__ import annotations
from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState
from trainos.kernel.logging.log_level import LogLevel
from trainos.kernel.logging.logger import Logger


class LogService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="logging",
            startup_priority=15,
            dependencies=("clock",),
        )
        self._logger = Logger()

    @property
    def logger(self) -> Logger:
        return self._logger

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(
            ServiceState.INITIALIZED,
        )

    def start(self) -> None:
        self._set_state(
            ServiceState.STARTING,
        )
        self._set_state(
            ServiceState.RUNNING,
        )

    def update(
        self,
        dt: float,
    ) -> None:
        pass

    def stop(self) -> None:
        self._set_state(
            ServiceState.STOPPING,
        )
        self._set_state(
            ServiceState.STOPPED,
        )

    def dispose(self) -> None:
        self._logger.clear()

    def health_check(self) -> bool:
        return not self.failed

    def set_level(
        self,
        level: LogLevel,
    ) -> None:
        self._logger.set_level(level)
