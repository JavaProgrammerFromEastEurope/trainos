from trainos.kernel.kernel import Kernel
from trainos.kernel.events.event import Event
from trainos.kernel.events.event_handler import EventHandler


class ReentrantHandler(EventHandler):

    def __init__(self, kernel: Kernel, events: list[int]):
        self._kernel = kernel
        self._events = events

    def handle(self, event: Event) -> None:
        self._events.append(event.payload)

        if event.payload == 1:
            self._kernel.event_bus.publish(
                Event(
                    event_type="e",
                    payload=2,
                    timestamp=0.0,
                )
            )


def test_reentrant_publish_during_update():
    k = Kernel()

    events: list[int] = []

    handler = ReentrantHandler(k, events)

    k.event_bus.subscribe("e", handler)

    k.event_bus.publish(
        Event(
            event_type="e",
            payload=1,
            timestamp=0.0,
        )
    )

    # первый тик
    k.event_bus.update()

    assert events == [1]

    # второй тик
    k.event_bus.update()

    assert events == [1, 2]
