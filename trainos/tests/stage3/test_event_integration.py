from trainos.kernel.state.state_service import StateService


def test_event_integration():

    state = StateService()
    state.initialize()
    state.start()
    events = []
    state._kernel = type(
        "K",
        (),
        {"publish": lambda self, e: events.append(e)},
    )()

    state.set("x", 1)

    assert len(events) == 1
    assert events[0].key == "x"
    assert events[0].new_value == 1
