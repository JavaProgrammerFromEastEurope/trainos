from __future__ import annotations

from .group_opinion import GroupOpinion


class OpinionPool:

    def __init__(self) -> None:
        self._opinions: list[GroupOpinion] = []

    def add(self, opinion: GroupOpinion) -> None:
        self._opinions.append(opinion)

    def all(self) -> tuple[GroupOpinion, ...]:
        return tuple(self._opinions)
