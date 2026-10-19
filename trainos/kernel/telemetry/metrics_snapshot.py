# kernel/telemetry/metrics_snapshot.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class MetricsSnapshot:
    timestamp: float
    metrics: dict[str, Any]

