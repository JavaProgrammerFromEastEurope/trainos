import pytest
from trainos.kernel.kernel import Kernel
from trainos.kernel.lifecycle.kernel_service import KernelService


class DummyService(KernelService):
    def __init__(self):
        super().__init__(name="dummy", dependencies=[])

    def initialize(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def update(self, dt):
        pass

    def dispose(self):
        pass


def test_register_and_get_service():
    k = Kernel()
    s = DummyService()

    k.register_service(s)

    assert k.get_service("dummy") == s


def test_duplicate_service_fails():
    k = Kernel()
    s = DummyService()

    k.register_service(s)

    with pytest.raises(ValueError):
        k.register_service(s)
