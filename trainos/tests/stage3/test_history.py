from trainos.kernel.state.state_service import StateService


def test_history():

    state = StateService()
    state.initialize()
    state.start()

    state.set("a", 1)
    state.set("a", 2)

    history = state.history.records

    assert len(history) == 2
    assert history[-1].new_value == 2
