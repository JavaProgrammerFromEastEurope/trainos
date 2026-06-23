from .evolution_metric import EvolutionMetric
from .metric_type import MetricType


class EvolutionMetricsEngine:

    def evaluate(self) -> EvolutionMetric:
        return EvolutionMetric(
            type=MetricType.STABILITY,
            value=1.0,
        )
