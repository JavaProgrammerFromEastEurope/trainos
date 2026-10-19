from __future__ import annotations

from .relation import (
    Relation,
)


class RelationGraph:

    def __init__(
        self,
    ) -> None:
        self._relations: list[Relation] = []

    def add(
        self,
        relation: Relation,
    ) -> None:
        self._relations.append(
            relation,
        )

    def remove(
        self,
        relation: Relation,
    ) -> None:
        if relation in self._relations:
            self._relations.remove(
                relation,
            )

    def relations(
        self,
    ) -> tuple[Relation, ...]:
        return tuple(
            self._relations,
        )
