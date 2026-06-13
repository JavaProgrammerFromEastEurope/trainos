from trainos.kernel.command_bus.query import Query
from trainos.kernel.command_bus.query_handler import QueryHandler
from trainos.kernel.command_bus.query_bus import QueryBus


class Q(Query):
    pass


class H(QueryHandler):
    def execute(self, query):
        return 42


def test_query_system():
    bus = QueryBus()
    bus.register(Q, H())
    result = bus.ask(Q())
    assert result == 42
