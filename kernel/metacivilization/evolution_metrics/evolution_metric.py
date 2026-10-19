from dataclasses import dataclass

from .metric_type import MetricType


@dataclass
class EvolutionMetric:

    type: MetricType
    value: float