from trainos.kernel.state.state_service import StateService


def test_control_layer():

    state = StateService()
    state.initialize()
    state.start()
    state.set("a", 1)

    controller = state.controller()
    controller.pause()
    state.set("a", 2)  # ignored

    assert state.get("a") == 1

    controller.resume()
    controller.reset()

    assert state.get("a") is None
