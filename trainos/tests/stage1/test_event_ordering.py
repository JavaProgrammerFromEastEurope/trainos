from trainos.kernel.kernel import Kernel
from trainos.kernel.events.event import Event
from trainos.kernel.events.event_handler import EventHandler


class Handler1(EventHandler):
    def __init__(self, result):
        self._result = result

    def handle(self, event: Event) -> None:
        self._result.append(1)


class Handler2(EventHandler):
    def __init__(self, result):
        self._result = result

    def handle(self, event: Event) -> None:
        self._result.append(2)


class Handler3(EventHandler):
    def __init__(self, result):
        self._result = result

    def handle(self, event: Event) -> None:
        self._result.append(3)


def test_event_ordering():
    k = Kernel()

    result = []

    h1 = Handler1(result)
    h2 = Handler2(result)
    h3 = Handler3(result)

    k.event_bus.subscribe("e", h1)
    k.event_bus.subscribe("e", h2)
    k.event_bus.subscribe("e", h3)

    event = Event(
        event_type="e",
        payload=None,
        timestamp=0.0,
    )

    k.event_bus.publish(event)
    k.event_bus.update()

    assert result == [1, 2, 3]
