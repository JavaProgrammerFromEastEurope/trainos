from __future__ import annotations

from trainos.kernel.state.debug.state_inspection_node import (
    StateInspectionNode,
)


class StateInspector:

    def __init__(
        self,
        state_service,
    ) -> None:

        self._state_service = state_service

    def inspect(
        self,
    ) -> list[StateInspectionNode]:

        result: list[StateInspectionNode] = []

        for key, value in self._state_service._data.items():

            result.append(
                StateInspectionNode(
                    key=key,
                    value=value,
                    value_type=type(
                        value,
                    ).__name__,
                )
            )

        return result

    def keys(
        self,
    ) -> tuple[str, ...]:

        return tuple(self._state_service._data.keys())

    def values(
        self,
    ) -> tuple[object, ...]:

        return tuple(self._state_service._data.values())

    def has(
        self,
        key: str,
    ) -> bool:

        return key in (self._state_service._data)

    def size(
        self,
    ) -> int:

        return len(self._state_service._data)

    def dump(
        self,
    ) -> dict[str, object]:

        return dict(self._state_service._data)
