from .configuration_runtime import ConfigurationRuntime
from .runtime_status import ConfigurationRuntimeStatus


class RuntimeEngine:

    def start(
        self,
        runtime: ConfigurationRuntime,
    ) -> ConfigurationRuntime:
        return ConfigurationRuntime(
            runtime_id=runtime.runtime_id,
            status=ConfigurationRuntimeStatus.RUNNING,
        )

    def pause(
        self,
        runtime: ConfigurationRuntime,
    ) -> ConfigurationRuntime:
        return ConfigurationRuntime(
            runtime_id=runtime.runtime_id,
            status=ConfigurationRuntimeStatus.PAUSED,
        )

    def stop(
        self,
        runtime: ConfigurationRuntime,
    ) -> ConfigurationRuntime:
        return ConfigurationRuntime(
            runtime_id=runtime.runtime_id,
            status=ConfigurationRuntimeStatus.STOPPED,
        )
