from kernel.logistics.runtime.logistics_runtime import LogisticsRuntime


def test_logistics_runtime():

    runtime = LogisticsRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None