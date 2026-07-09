from kernel.consumption.runtime.consumption_runtime import ConsumptionRuntime


def test_consumption_runtime():

    runtime = ConsumptionRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()
    assert runtime.context is not None