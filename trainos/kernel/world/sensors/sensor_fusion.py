from __future__ import annotations

from .sensor_snapshot import (
    SensorSnapshot,
)

from .sensor_fusion_result import (
    SensorFusionResult,
)


class SensorFusion:

    def fuse(
        self,
        snapshot: SensorSnapshot,
    ) -> SensorFusionResult:
        return SensorFusionResult(
            perception=snapshot,
        )
