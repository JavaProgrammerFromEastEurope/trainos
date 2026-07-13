from dataclasses import dataclass

from .timer_configuration import TimerConfiguration


@dataclass(slots=True)
class TimerContext:

    configuration: TimerConfiguration
