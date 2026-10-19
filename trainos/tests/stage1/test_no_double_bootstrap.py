import pytest


def test_double_bootstrap(kernel):
    with pytest.raises(Exception):
        kernel.bootstrap()
        kernel.bootstrap()
