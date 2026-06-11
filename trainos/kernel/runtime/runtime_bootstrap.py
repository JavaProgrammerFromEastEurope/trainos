# kernel/runtime/runtime_bootstrap.py

from __future__ import annotations

from trainos.kernel.runtime.runtime_kernel import RuntimeKernel


def create_runtime_kernel() -> RuntimeKernel:
    kernel = RuntimeKernel()
    kernel.initialize()
    kernel.start()
    return kernel
