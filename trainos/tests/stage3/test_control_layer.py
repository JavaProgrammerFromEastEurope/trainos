from trainos.kernel.state.state_service import StateService


def test_control_layer():

    state = StateService()

    state.initialize()
    state.start()

    state.set("a", 1)

    controller = state.controller()

    # pause
    controller.pause()

    state.set("a", 2)

    assert state.get("a") == 1

    # resume
    controller.resume()

    state.set("a", 3)

    assert state.get("a") == 3

    # reset
    controller.reset()

    assert state.get("a") is None
