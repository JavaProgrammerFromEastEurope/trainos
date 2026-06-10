from trainos.kernel.kernel import Kernel
from trainos.kernel.events.event import Event
from trainos.kernel.events.event_handler import EventHandler


class SubscriberA(EventHandler):
    def __init__(self, out):
        self._out = out

    def handle(self, event: Event) -> None:
        self._out.append(("a", event))


class SubscriberB(EventHandler):
    def __init__(self, out):
        self._out = out

    def handle(self, event: Event) -> None:
        self._out.append(("b", event))


def test_multiple_subscribers():
    k = Kernel()

    out = []

    h1 = SubscriberA(out)
    h2 = SubscriberB(out)

    k.event_bus.subscribe("x", h1)
    k.event_bus.subscribe("x", h2)

    event = Event(
        event_type="x",
        payload=123,
        timestamp=0.0,
    )

    k.event_bus.publish(event)
    k.event_bus.update()

    assert len(out) == 2

    assert out[0][0] == "a"
    assert out[0][1].event_type == "x"
    assert out[0][1].payload == 123

    assert out[1][0] == "b"
    assert out[1][1].event_type == "x"
    assert out[1][1].payload == 123
