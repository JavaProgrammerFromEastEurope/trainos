from trainos.kernel.kernel import Kernel


def test_event_queue_does_not_crash_under_load():
    k = Kernel()

    def handler(e):
        pass

    k.event_bus.subscribe("e", handler)

    for i in range(1000):
        k.event_bus.publish("e", i)

    k.event_bus.update()

    assert True
