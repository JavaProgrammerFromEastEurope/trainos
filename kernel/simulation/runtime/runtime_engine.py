from .runtime_status import RuntimeStatus


class RuntimeEngine:

    def start(
        self,
        runtime,
    ):
        return runtime.__class__(
            runtime_id=runtime.runtime_id,
            status=RuntimeStatus.RUNNING,
        )

    def pause(
        self,
        runtime,
    ):
        return runtime.__class__(
            runtime_id=runtime.runtime_id,
            status=RuntimeStatus.PAUSED,
        )

    def stop(
        self,
        runtime,
    ):
        return runtime.__class__(
            runtime_id=runtime.runtime_id,
            status=RuntimeStatus.STOPPED,
        )
