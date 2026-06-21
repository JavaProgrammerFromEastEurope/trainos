from dataclasses import dataclass


@dataclass
class ResourceUsageMetrics:

    production_rate: 	float
    consumption_rate: float
    loss_rate: float