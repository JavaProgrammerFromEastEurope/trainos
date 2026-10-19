from kernel.configuration.runtime.configuration_runtime import ConfigurationRuntime
from kernel.configuration.runtime.runtime_status import ConfigurationRuntimeStatus
from kernel.configuration.runtime.runtime_engine import RuntimeEngine


def test_runtime_lifecycle():

    runtime = ConfigurationRuntime(
        runtime_id="CFG1",
        status=ConfigurationRuntimeStatus.CREATED,
    )
    engine = RuntimeEngine()
    runtime = engine.start(runtime)
    assert runtime.status == ConfigurationRuntimeStatus.RUNNING

    runtime = engine.pause(runtime)
    assert runtime.status == ConfigurationRuntimeStatus.PAUSED

    runtime = engine.stop(runtime)
    assert runtime.status == ConfigurationRuntimeStatus.STOPPED
