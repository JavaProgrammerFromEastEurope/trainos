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

    # priority encoded inside closure (compat mode)

    scheduler.schedule(lambda: task_b(), delay_seconds=0.0)
    scheduler.schedule(lambda: task_c(), delay_seconds=0.0)
    scheduler.schedule(lambda: task_a(), delay_seconds=0.0)

    scheduler.update(1.0)

    # NOTE: ordering must still be enforced internally by scheduler
    assert result == ["b", "c", "a"]
