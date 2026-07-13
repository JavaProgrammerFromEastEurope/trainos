from kernel.scheduling.runtime.timer_runtime import TimerRuntime

from kernel.scheduling.runtime.timer_engine import TimerEngine
from kernel.scheduling.runtime.timer_status import TimerStatus


def test_timer_runtime():

    runtime = TimerRuntime(
        runtime_id="TIMER-001",
    )
    engine = TimerEngine()
    runtime = engine.start(runtime)
    assert runtime.status == TimerStatus.RUNNING

    runtime = engine.tick(runtime)
    assert runtime.tick == 1

    runtime = engine.stop(runtime)
    assert runtime.status == TimerStatus.STOPPED
