from trainos.kernel.command_bus.middleware_chain import MiddlewareChain
from trainos.kernel.command_bus.request import Request
from trainos.kernel.command_bus.response import Response


class MW:
    def handle(self, request, next_call):
        request.payload["mw"] = True
        return next_call(request)


def test_middleware():
    def final(req):
        return Response(True, req.payload)

    chain = MiddlewareChain([MW()], final)
    res 	= chain.execute(Request({"a": 1}))
    assert res.data["mw"] is True