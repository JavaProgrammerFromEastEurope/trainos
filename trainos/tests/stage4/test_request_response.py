from trainos.kernel.command_bus.request import Request
from trainos.kernel.command_bus.response import Response


def test_request_response():

    req = Request({"x": 1})
    res = Response(True, {"y": 2})
    assert req.payload["x"] == 1
    assert res.success is True
