from __future__ import annotations

from .episode import Episode


class EpisodeHistory:

    def __init__(self) -> None:
        self._history: list[Episode] = []

    def add(self, episode: Episode) -> None:
        self._history.append(episode)

    def episodes(self) -> tuple[Episode, ...]:
        return tuple(self._history)
