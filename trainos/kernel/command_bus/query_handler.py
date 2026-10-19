from __future__ import annotations

from abc import ABC, abstractmethod
from .query import Query


class QueryHandler(ABC):

    @abstractmethod
    def execute(
        self,
        query: Query,
    ):
        pass
