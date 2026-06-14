from dataclasses import dataclass

from .world_metrics import (
    WorldMetrics,
)


@dataclass
class WorldContext:
    metrics: WorldMetrics