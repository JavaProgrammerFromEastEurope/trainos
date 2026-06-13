from __future__ import annotations

from trainos.kernel.state.serialization.state_serializer import (
    StateSerializer,
)


class StateImporter:

    def __init__(self) -> None:
        self._serializer = StateSerializer()

    def import_state(self, data: str) -> dict:
        return self._serializer.deserialize(data)
