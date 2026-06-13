from trainos.kernel.state.state_service import StateService


def test_reactive_state_system():

    state = StateService()
    state.initialize()
    state.start()
    state.set("hp", 100)
    state.set("hp", 80)

    snapshot = state.snapshot()

    assert snapshot.data["hp"] == 80
    assert len(snapshot.changes) == 2
