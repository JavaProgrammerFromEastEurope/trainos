from kernel.events.event import Event
from kernel.events.event_bus import EventBus
from kernel.scheduler.event_scheduler import EventScheduler
from kernel.scheduler.priority import Priority, ScheduledTask


class RecordingHandler:
    def __init__(self):
        self.events = []

    def handle(self, event):
        self.events.append(event)


def test_event_scheduler_publishes_only_due_events_and_preserves_future_events():
    bus = EventBus()
    handler = RecordingHandler()
    bus.subscribe("heartbeat", handler)
    scheduler = EventScheduler(bus)

    due = Event("heartbeat", {"id": "due"})
    future = Event("heartbeat", {"id": "future"})
    scheduler.schedule(
        ScheduledTask("due-task", Priority.NORMAL, 5.0, {"event": due})
    )
    scheduler.schedule(
        ScheduledTask("future-task", Priority.CRITICAL, 10.0, {"event": future})
    )

    scheduler.update(5.0)
    bus.update()
    assert handler.events == [due]

    scheduler.update(10.0)
    bus.update()
    assert handler.events == [due, future]
