from trainos.kernel.state.state_service import StateService


def test_transactions():

    state = StateService()
    state.initialize()
    state.start()
    state.set("x", 1)

    tx = state.transaction()
    tx.rollback()

    assert state.get("x") == 1