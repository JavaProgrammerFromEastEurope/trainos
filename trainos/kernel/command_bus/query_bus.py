from __future__ import annotations

from typing import Type
from .query import Query
from .query_handler import QueryHandler


class QueryBus:

    def __init__(self) -> None:
        self._handlers: dict[
            Type[Query],
            QueryHandler,
        ] = {}

    def register(
        self,
        query_type: Type[Query],
        handler: QueryHandler,
    ) -> None:
        self._handlers[query_type] = handler

    def ask(
        self,
        query: Query,
    ):
        handler = self._handlers.get(
            type(query),
        )
        if handler is None:
            raise Exception(
                f"No handler for {type(query)}",
            )
        return handler.execute(
            query,
        )
