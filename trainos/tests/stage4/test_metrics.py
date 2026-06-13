from trainos.kernel.command_bus.command_metrics import CommandMetrics


def test_metrics():

    m = CommandMetrics()
    m.record_success("A")
    m.record_error("B")

    assert m.total_executed == 2
    assert m.success_count 	== 1
    assert m.error_count 		== 1