from .timer_runtime import TimerRuntime

from .timer_status import TimerStatus


class TimerEngine:

    def start(
        self,
        runtime: TimerRuntime,
    ) -> TimerRuntime:
        return TimerRuntime(
            runtime_id=runtime.runtime_id,
            tick=runtime.tick,
            status=TimerStatus.RUNNING,
        )

    def tick(
        self,
        runtime: TimerRuntime,
    ) -> TimerRuntime:
        return TimerRuntime(
            runtime_id=runtime.runtime_id,
            tick=runtime.tick + 1,
            status=runtime.status,
        )

    def stop(
        self,
        runtime: TimerRuntime,
    ) -> TimerRuntime:
        return TimerRuntime(
            runtime_id=runtime.runtime_id,
            tick=runtime.tick,
            status=TimerStatus.STOPPED,
        )
