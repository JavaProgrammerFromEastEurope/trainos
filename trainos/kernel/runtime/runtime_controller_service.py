# kernel/runtime/runtime_controller_service.py

from __future__ import annotations

from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)
from trainos.kernel.runtime.runtime_state import RuntimeState


class RuntimeControllerService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="runtime_controller",
            dependencies=(),
        )
        self._runtime_state = RuntimeState.CREATED

    @property
    def runtime_state(self) -> RuntimeState:
        return self._runtime_state

    @property
    def is_running(self) -> bool:
        return self._runtime_state == RuntimeState.RUNNING

    @property
    def is_paused(self) -> bool:
        return self._runtime_state == RuntimeState.PAUSED

    @property
    def is_stopped(self) -> bool:
        return self._runtime_state == RuntimeState.STOPPED

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._runtime_state = RuntimeState.RUNNING
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._runtime_state = RuntimeState.STOPPED
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._runtime_state = RuntimeState.CREATED

    def update(self, dt: float) -> None:
        return

    def pause(self) -> None:
        if self._runtime_state == RuntimeState.RUNNING:
            self._runtime_state = RuntimeState.PAUSED

    def resume(self) -> None:
        if self._runtime_state == RuntimeState.PAUSED:
            self._runtime_state = RuntimeState.RUNNING
