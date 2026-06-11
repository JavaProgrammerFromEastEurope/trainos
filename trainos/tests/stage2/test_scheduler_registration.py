# tests/stage2/test_scheduler_registration.py

from trainos.kernel.scheduler.scheduler_service import SchedulerService
from trainos.kernel.lifecycle.kernel_service import ServiceState


def test_scheduler_registration():

    scheduler = SchedulerService()
    scheduler.initialize()
    scheduler.start()

    executed = []

    def task_a():
        executed.append("a")

    def task_b():
        executed.append("b")

    handle_a = scheduler.schedule(task_a)
    handle_b = scheduler.schedule(task_b)

    assert scheduler.state == ServiceState.RUNNING
    assert scheduler.task_count == 2
    scheduler.update(0.1)
    assert executed == ["a", "b"]
    scheduler.cancel(handle_a)
    assert scheduler.task_count == 1
    scheduler.cancel(handle_b)
    assert scheduler.task_count == 0
