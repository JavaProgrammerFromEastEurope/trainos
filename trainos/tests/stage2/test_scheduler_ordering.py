# tests/stage2/test_scheduler_ordering.py

from trainos.kernel.scheduler.scheduler_service import SchedulerService


def test_scheduler_ordering():

    scheduler = SchedulerService()

    scheduler.initialize()
    scheduler.start()

    result = []

    def task_a():
        result.append("a")

    def task_b():
        result.append("b")

    def task_c():
        result.append("c")

    scheduler.schedule(
        task_b,
        delay_seconds=1.0,
    )

    scheduler.schedule(
        task_c,
        delay_seconds=1.0,
    )

    scheduler.schedule(
        task_a,
        delay_seconds=1.0,
    )

    scheduler.update(0.5)

    assert result == []

    scheduler.update(0.5)

    assert result == ["b", "c", "a"]