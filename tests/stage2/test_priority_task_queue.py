from kernel.scheduler.priority import Priority, ScheduledTask
from kernel.scheduler.task_queue import TaskQueue


def test_priority_queue_orders_by_priority_then_timestamp():
    queue = TaskQueue()
    low = ScheduledTask("low", Priority.LOW, 1.0, {})
    early_high = ScheduledTask("early-high", Priority.HIGH, 1.0, {})
    late_high = ScheduledTask("late-high", Priority.HIGH, 2.0, {})

    queue.push(low)
    queue.push(late_high)
    queue.push(early_high)

    assert [queue.pop().task_id for _ in range(3)] == [
        "early-high",
        "late-high",
        "low",
    ]
    assert queue.empty()


def test_priority_queue_is_fifo_for_equal_priority_and_timestamp():
    queue = TaskQueue()
    first = ScheduledTask("first", Priority.NORMAL, 5.0, {})
    second = ScheduledTask("second", Priority.NORMAL, 5.0, {})

    queue.push(first)
    queue.push(second)

    assert queue.pop() is first
    assert queue.pop() is second
    assert queue.peek() is None


def test_priority_queue_can_pop_due_task_without_blocking_on_future_priority():
    queue = TaskQueue()
    future_critical = ScheduledTask("future", Priority.CRITICAL, 100.0, {})
    due_low = ScheduledTask("due", Priority.LOW, 1.0, {})
    queue.push(future_critical)
    queue.push(due_low)

    assert queue.pop_due(1.0) is due_low
    assert queue.peek() is future_critical
    assert queue.pop_due(1.0) is None
