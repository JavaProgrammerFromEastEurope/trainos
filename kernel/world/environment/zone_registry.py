from __future__ import annotations

from .environment_zone import (
    EnvironmentZone,
)


class ZoneRegistry:

    def __init__(self):
        self._zones: dict[
            str,
            EnvironmentZone,
        ] = {}

    def register(
        self,
        zone: EnvironmentZone,
    ) -> None:
        self._zones[zone.name] = zone

    def get(
        self,
        name: str,
    ):
        return self._zones.get(
            name,
        )
