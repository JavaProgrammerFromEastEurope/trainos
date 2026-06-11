import pytest

from trainos.kernel.kernel import Kernel


@pytest.fixture
def kernel():
    k = Kernel()
    k.initialize()
    k.start()
    return k
