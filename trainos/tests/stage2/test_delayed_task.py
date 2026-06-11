# tests/stage2/test_delayed_task.py

from trainos.kernel.scheduler.scheduler_service import SchedulerService


def test_delayed_task():

    scheduler = SchedulerService()
    scheduler.initialize()
    scheduler.start()
    calls = []

    def task():
        calls.append(1)

    # task should NOT execute before delay
    scheduler.schedule(
        task,
        delay_seconds=1.0,
    )

    scheduler.update(0.5)
    assert calls == []

    scheduler.update(0.5)
    assert calls == [1]
