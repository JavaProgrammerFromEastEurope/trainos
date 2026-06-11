# tests/stage2/test_periodic_task.py

from trainos.kernel.scheduler.scheduler_service import SchedulerService


def test_periodic_task():

    scheduler = SchedulerService()

    scheduler.initialize()
    scheduler.start()

    calls = []

    def task():
        calls.append(1)

    scheduler.schedule(
        task,
        delay_seconds=0.0,
        interval_seconds=1.0,
        repeat=True,
    )

    # t = 0.5 → ещё не должен сработать
    scheduler.update(0.5)
    assert len(calls) == 0

    # t = 1.0 → первая сработка
    scheduler.update(0.5)
    assert len(calls) == 1

    # t = 2.0 → вторая сработка
    scheduler.update(1.0)
    assert len(calls) == 2

    # t = 3.0 → третья сработка
    scheduler.update(1.0)
    assert len(calls) == 3
