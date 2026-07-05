from kernel.resources.runtime.resources_runtime import ResourcesRuntime


def test_resources_runtime():

    runtime = ResourcesRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()
    
    assert runtime.context is not None