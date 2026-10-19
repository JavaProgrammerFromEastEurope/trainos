from __future__ import annotations

from .epoch import (
    Epoch,
)


class EpochHistory:

    def __init__(
        self,
    ) -> None:
        self._epochs: list[Epoch] = []

    def add(
        self,
        epoch: Epoch,
    ) -> None:
        self._epochs.append(epoch)

    def epochs(
        self,
    ) -> tuple[Epoch, ...]:
        return tuple(self._epochs)
