from __future__ import annotations


class Query:
    """
    Base query object (read-side request).
    """

    def __init__(self) -> None:
        self._name: str = self.__class__.__name__

    @property
    def name(self) -> str:
        return self._name