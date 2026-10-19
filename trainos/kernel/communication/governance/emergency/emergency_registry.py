from __future__ import annotations

from .emergency_protocol import EmergencyProtocol


class EmergencyRegistry:

    def __init__(self) -> None:
        self._protocols: list[EmergencyProtocol] = []

    def add(self, protocol: EmergencyProtocol) -> None:
        self._protocols.append(protocol)

    def protocols(self) -> tuple[EmergencyProtocol, ...]:
        return tuple(self._protocols)
