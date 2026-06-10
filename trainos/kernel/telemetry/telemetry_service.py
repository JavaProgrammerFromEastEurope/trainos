# kernel/telemetry/telemetry_service.py

from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict

from trainos.kernel.lifecycle.kernel_service import KernelService
from trainos.kernel.lifecycle.kernel_service import ServiceState
from trainos.kernel.telemetry.metric_record import MetricRecord
from trainos.kernel.telemetry.metrics_snapshot import MetricsSnapshot


class TelemetryService(KernelService):

    def __init__(self) -> None:
        super().__init__(
            name="telemetry",
            startup_priority=40,
            dependencies=("clock",),
        )
        self._metrics: DefaultDict[str, list[MetricRecord]] = defaultdict(list)

    def initialize(self) -> None:
        self._metrics.clear()
        self._mark_initialized()
        self._set_state(ServiceState.INITIALIZED)

    def start(self) -> None:
        self._set_state(ServiceState.STARTING)
        self._set_state(ServiceState.RUNNING)

    def stop(self) -> None:
        self._set_state(ServiceState.STOPPING)
        self._set_state(ServiceState.STOPPED)

    def dispose(self) -> None:
        self._metrics.clear()

    def update(self, dt: float) -> None:
        pass

    def record(
        self,
        name: str,
        value: float,
        timestamp: float,
    ) -> None:
        self._metrics[name].append(
            MetricRecord(
                name=name,
                value=value,
                timestamp=timestamp,
            )
        )

    def latest(self, name: str) -> float | None:
        records = self._metrics.get(name)
        if not records:
            return None
        return records[-1].value

    def average(self, name: str) -> float:
        records = self._metrics.get(name)
        if not records:
            return 0.0
        return sum(record.value for record in records) / len(records)

    def snapshot(self, timestamp: float) -> MetricsSnapshot:
        data: dict[str, float] = {}
        for metric_name, records in self._metrics.items():
            if records:
                data[metric_name] = records[-1].value
        return MetricsSnapshot(
            timestamp=timestamp,
            metrics=data,
        )

    def health_check(self) -> bool:
        return not self.failed
