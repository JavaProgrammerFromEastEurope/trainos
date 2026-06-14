from __future__ import annotations

from .world_runtime import (
    WorldRuntime,
)
from .world_metrics import (
    WorldMetrics,
)


class WorldRuntimeService:

    def __init__(
        self,
    ) -> None:
        self._runtime = WorldRuntime()
        self._metrics = WorldMetrics()

    @property
    def runtime(
        self,
    ) -> WorldRuntime:
        return self._runtime

    @property
    def metrics(
        self,
    ) -> WorldMetrics:
        return self._metrics
