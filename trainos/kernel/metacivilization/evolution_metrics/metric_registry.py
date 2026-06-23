from __future__ import annotations

from .evolution_metric import EvolutionMetric


class MetricRegistry:

    def __init__(self) -> None:
        self._metrics: list[EvolutionMetric] = []

    def register(self, metric: EvolutionMetric) -> None:
        self._metrics.append(metric)

    def metrics(self) -> tuple[EvolutionMetric, ...]:
        return tuple(self._metrics)
