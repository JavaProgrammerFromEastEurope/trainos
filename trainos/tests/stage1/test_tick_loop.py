from trainos.kernel.kernel import Kernel
from trainos.kernel.lifecycle.kernel_service import (
    KernelService,
    ServiceState,
)


class DummyService(KernelService):

    def __init__(self, calls):
        super().__init__(
            name="s",
            dependencies=(),
        )
        self._calls = calls

    def initialize(self) -> None:
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        pass

    def update(self, dt: float) -> None:
        self._calls.append(dt)


def test_tick_loop_executes_services():
    calls = []

    k = Kernel()

    service = DummyService(calls)

    k.register_service(service)

    k.initialize()
    k.start()

    k.update(0.016)

    assert calls == [0.016]
