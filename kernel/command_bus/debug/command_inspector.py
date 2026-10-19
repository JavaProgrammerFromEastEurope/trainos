from __future__ import annotations

from typing import List
from ..command_history import CommandHistory
from .command_inspection_node import CommandInspectionNode


class CommandInspector:

    def __init__(
        self,
        history: CommandHistory,
    ) -> None:
        self._history = history

    def inspect(self) -> List[CommandInspectionNode]:
        result: List[CommandInspectionNode] = []
        for record in self._history.all():
            result.append(
                CommandInspectionNode(
                    command_name=record.command_name,
                    timestamp=record.timestamp,
                    success=record.success,
                    metadata={
                        "payload": record.payload,
                        "error": record.error,
                    },
                )
            )
        return result
