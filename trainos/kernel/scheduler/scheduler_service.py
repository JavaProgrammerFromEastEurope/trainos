from __future__ import annotations

from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState
from trainos.kernel.scheduler.event_scheduler import EventScheduler
from trainos.kernel.scheduler.interrupt_controller import InterruptController
from trainos.kernel.events.event_bus import EventBus


class SchedulerService(KernelService):

    def __init__(self, event_bus: EventBus) -> None:

        super().__init__(
            name="scheduler",
            startup_priority=5,
            dependencies=("clock", "events"),
        )

        self._scheduler = EventScheduler(event_bus)
        self._interrupts = InterruptController()

    def initialize(self) -> None:

        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:

        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def update(self, dt: float) -> None:

        self._scheduler.update(now=dt)

    def stop(self) -> None:

        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        pass

    @property
    def scheduler(self) -> EventScheduler:
        return self._scheduler

    @property
    def interrupts(self) -> InterruptController:
        return self._interrupts
