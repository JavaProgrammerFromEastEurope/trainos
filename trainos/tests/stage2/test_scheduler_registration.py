# tests/stage2/test_scheduler_registration.py

from trainos.kernel.scheduler.scheduler_service import SchedulerService


def test_scheduler_registration():

    scheduler = SchedulerService()

    scheduler.initialize()
    scheduler.start()

    calls = []

    def task():
        calls.append(1)

    scheduler.schedule(
        task,
        delay_seconds=1.0,
    )

    assert len(calls) == 0

    scheduler.update(0.5)

    assert len(calls) == 0

    scheduler.update(0.5)

    assert len(calls) == 1