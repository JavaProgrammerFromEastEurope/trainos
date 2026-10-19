from __future__ import annotations

from .episode_step import EpisodeStep


class Episode:

    def __init__(self) -> None:
        self._steps: list[EpisodeStep] = []

    def add_step(self, step: EpisodeStep) -> None:
        self._steps.append(step)

    def steps(self) -> tuple[EpisodeStep, ...]:
        return tuple(self._steps)
