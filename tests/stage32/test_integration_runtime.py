from kernel.integration.runtime.integration_runtime import IntegrationRuntime
from kernel.integration.runtime.runtime_engine import IntegrationRuntimeEngine
from kernel.integration.runtime.runtime_status import IntegrationRuntimeStatus


def test_integration_runtime():

    runtime = IntegrationRuntime(
        runtime_id="RT1",
        status=IntegrationRuntimeStatus.CREATED,
    )
    engine = IntegrationRuntimeEngine()
    runtime = engine.start(runtime)
    assert runtime.status == IntegrationRuntimeStatus.RUNNING

    runtime = engine.pause(runtime)
    assert runtime.status == IntegrationRuntimeStatus.PAUSED

    runtime = engine.stop(runtime)
    assert runtime.status == IntegrationRuntimeStatus.STOPPED
