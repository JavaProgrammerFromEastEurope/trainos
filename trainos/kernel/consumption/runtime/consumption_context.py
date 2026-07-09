from dataclasses import dataclass

from .consumption_configuration import ConsumptionConfiguration


@dataclass(slots=True)
class ConsumptionContext:

    configuration: ConsumptionConfiguration
