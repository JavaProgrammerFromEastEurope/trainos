from __future__ import annotations

from .sensor import Sensor


class SensorRegistry:

    def __init__(
        self,
    ) -> None:

        self._sensors: list[Sensor] = []

    def register(
        self,
        sensor: Sensor,
    ) -> None:

        self._sensors.append(
            sensor,
        )

    def sensors(
        self,
    ) -> tuple[Sensor, ...]:

        return tuple(
            self._sensors,
        )
