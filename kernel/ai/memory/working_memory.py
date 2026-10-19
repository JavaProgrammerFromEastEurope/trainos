from __future__ import annotations

from typing import Dict, Any


class WorkingMemory:

    def __init__(self) -> None:
        self._memory: Dict[
            str,
            Any,
        ] = {}

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        self._memory[key] = value

    def get(
        self,
        key: str,
        default=None,
    ):
        return self._memory.get(
            key,
            default,
        )

    def clear(self) -> None:
        self._memory.clear()
