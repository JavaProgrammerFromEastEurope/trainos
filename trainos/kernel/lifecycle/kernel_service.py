# kernel/lifecycle/kernel_service.py

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class ServiceState(Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class ServiceStatus:
    name: str
    state: ServiceState
    healthy: bool
    uptime_seconds: float
    failure_reason: str | None = None


class KernelService(ABC):

    def __init__(
        self,
        name: str,
        startup_priority: int = 0,
        dependencies: Tuple[str, ...] = (),
    ) -> None:

        self._name = name
        self._startup_priority = startup_priority
        self._dependencies = dependencies

        self._state = ServiceState

        self._initialized = False
        self._failed = False

        self._uptime_seconds = 0.0
        self._failure_reason: str | None = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> ServiceState:
        return self._state

    @property
    def startup_priority(self) -> int:
        return self._startup_priority

    @property
    def dependencies(self) -> Tuple[str, ...]:
        return self._dependencies

    @property
    def initialized(self) -> bool:
        return self._initialized

    @property
    def failed(self) -> bool:
        return self._failed

    @property
    def failure_reason(self) -> str | None:
        return self._failure_reason

    def set_uptime(self, uptime_seconds: float) -> None:
        self._uptime_seconds = uptime_seconds

    @abstractmethod
    def initialize(self) -> None: ...

    @abstractmethod
    def start(self) -> None: ...

    def update(self, dt: float) -> None:
        return

    @abstractmethod
    def stop(self) -> None: ...

    def dispose(self) -> None:
        return

    def health_check(self) -> bool:
        return not self._failed

    def status(self) -> ServiceStatus:

        return ServiceStatus(
            name=self._name,
            state=self._state,
            healthy=self.health_check(),
            uptime_seconds=self._uptime_seconds,
            failure_reason=self._failure_reason,
        )

    def _set_state(self, state: ServiceState) -> None:
        self._state = state

    def _mark_initialized(self) -> None:
        self._initialized = True

    def _mark_failed(self, reason: str) -> None:

        self._failed = True
        self._failure_reason = reason
        self._state = ServiceState.FAILED
