# kernel/runtime/runtime_snapshot.py

from __future__ import annotations

from dataclasses import dataclass

from kernel.health.health_report 		import HealthReport
from kernel.runtime.runtime_metrics import RuntimeMetrics
from kernel.runtime.runtime_state 	import RuntimeState


@dataclass(frozen=True, slots=True)
class RuntimeSnapshot:
    state: RuntimeState
    metrics: RuntimeMetrics
    health: HealthReport
