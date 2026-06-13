from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class StateInspectionNode:

    key: str
    value: Any
    type_name: str


class StateInspector:

    def __init__(
        self,
        state_service,
    ) -> None:
        self._state_service = state_service

    def inspect(self) -> list[StateInspectionNode]:
        result: list[StateInspectionNode] = []
        for key, value in self._state_service._state.items():
            result.append(
                StateInspectionNode(
                    key=key,
                    value=value,
                    type_name=type(value).__name__,
                )
            )
        return result

    def dump(self) -> dict[str, Any]:
        return {key: value for key, value in self._state_service._state.items()}

    def find(
        self,
        prefix: str,
    ) -> list[StateInspectionNode]:
        result: list[StateInspectionNode] = []
        for key, value in self._state_service._state.items():
            if not key.startswith(prefix):
                continue
            result.append(
                StateInspectionNode(
                    key=key,
                    value=value,
                    type_name=type(value).__name__,
                )
            )
        return result
