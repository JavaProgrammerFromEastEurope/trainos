from __future__ import annotations

from .self_play_match import SelfPlayMatch


class SelfPlayHistory:

    def __init__(
        self,
    ) -> None:
        self._matches: list[SelfPlayMatch] = []

    def add(
        self,
        match: SelfPlayMatch,
    ) -> None:
        self._matches.append(match)

    def matches(
        self,
    ) -> tuple[SelfPlayMatch, ...]:
        return tuple(self._matches)
