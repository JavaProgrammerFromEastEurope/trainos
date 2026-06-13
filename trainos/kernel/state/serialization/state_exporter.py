from __future__ import annotations

from trainos.kernel.state.serialization.state_serializer import (
    StateSerializer,
)


class StateExporter:

    def __init__(self) -> None:
        self._serializer = StateSerializer()

    def export(self, state: dict) -> str:
        return self._serializer.serialize(state)
