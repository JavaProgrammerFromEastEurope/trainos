from __future__ import annotations

from typing import List
from .undoable_command import UndoableCommand


class CommandStack:

    def __init__(self) -> None:
        self._executed: List[UndoableCommand] = []
        self._undone: 	List[UndoableCommand] = []

    def push(
        self,
        command: UndoableCommand,
    ) -> None:
        self._executed.append(command)
        self._undone.clear()

    def undo(self) -> UndoableCommand | None:
        if not self._executed:
            return None
        cmd = self._executed.pop()
        cmd.undo()
        self._undone.append(cmd)
        return cmd

    def redo(self) -> UndoableCommand | None:
        if not self._undone:
            return None
        cmd = self._undone.pop()
        self._executed.append(cmd)
        return cmd

    def clear(self) -> None:
        self._executed.clear()
        self._undone.clear()
