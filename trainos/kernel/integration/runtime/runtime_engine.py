from .integration_runtime import IntegrationRuntime
from .runtime_status 			import IntegrationRuntimeStatus


class IntegrationRuntimeEngine:

    def start(
        self,
        runtime: IntegrationRuntime,
    ) -> IntegrationRuntime:
        return IntegrationRuntime(
            runtime_id=runtime.runtime_id,
            status=IntegrationRuntimeStatus.RUNNING,
        )

    def pause(
        self,
        runtime: IntegrationRuntime,
    ) -> IntegrationRuntime:
        return IntegrationRuntime(
            runtime_id=runtime.runtime_id,
            status=IntegrationRuntimeStatus.PAUSED,
        )

    def stop(
        self,
        runtime: IntegrationRuntime,
    ) -> IntegrationRuntime:
        return IntegrationRuntime(
            runtime_id=runtime.runtime_id,
            status=IntegrationRuntimeStatus.STOPPED,
        )
