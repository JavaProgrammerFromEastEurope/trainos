import pytest
from trainos.kernel.kernel import Kernel
from trainos.kernel.lifecycle.kernel_service import KernelService


class DummyService(KernelService):
    def __init__(self):
        super().__init__(name="dummy", dependencies=[])

        # ❗ вместо self.initialized = False
        self._initialized = False
        self._started = False
        self._stopped = False

    def initialize(self):
        self._initialized = True

    def start(self):
        self._started = True

    def stop(self):
        self._stopped = True

    def update(self, dt):
        pass

    def dispose(self):
        pass


@pytest.fixture
def kernel():
    return Kernel()


@pytest.fixture
def service():
    return DummyService()


def test_service_lifecycle_order(kernel, service):
    kernel.register_service(service)

    kernel.initialize()
    kernel.start()

    assert service._initialized is True
    assert service._started is True

    kernel.stop()
    assert service._stopped is True