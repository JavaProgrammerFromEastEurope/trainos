from abc import ABC, abstractmethod

from .base_context import BaseContext


class BaseEngine(ABC):

    @abstractmethod
    def initialize(
        self,
        context: BaseContext,
    ) -> None:
        pass

    @abstractmethod
    def update(
        self,
        context: BaseContext,
        *args,
        **kwargs,
    ) -> None:
        pass

    @abstractmethod
    def shutdown(
        self,
        context: BaseContext,
    ) -> None:
        pass
