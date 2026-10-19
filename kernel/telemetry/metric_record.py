# kernel/telemetry/metric_record.py

from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class MetricRecord:
    name: str
    value: float
    timestamp: float
