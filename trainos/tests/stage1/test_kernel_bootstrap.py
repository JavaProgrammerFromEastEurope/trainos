from trainos.kernel.kernel import Kernel


def test_kernel_bootstrap():
    k = Kernel()
    k.bootstrap()

    assert k.is_booted() is True