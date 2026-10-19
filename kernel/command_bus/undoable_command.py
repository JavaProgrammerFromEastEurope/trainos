from __future__ import annotations

from abc import ABC, abstractmethod

from .command import Command


class UndoableCommand(Command, ABC):

    @abstractmethod
    def undo(self) -> None:
        pass
