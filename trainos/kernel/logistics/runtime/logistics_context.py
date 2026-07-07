from dataclasses import dataclass

from .logistics_configuration import LogisticsConfiguration


@dataclass(slots=True)
class LogisticsContext:

    configuration: LogisticsConfiguration
