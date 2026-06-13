from trainos.kernel.state.state_service import StateService


def test_inspector():

    state = StateService()
    state.initialize()
    state.start()

    state.set("hp", 100)

    inspector = state.inspector()

    result = inspector.inspect()

    assert len(result) == 1
    assert result[0].key == "hp"
