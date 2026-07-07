from kernel.production.runtime.production_runtime import ProductionRuntime


def test_production_runtime():

    runtime = ProductionRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None