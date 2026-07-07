from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LogisticsConfiguration:

    auto_start: 						bool = True
    max_parallel_deliveries: int = 8
    enable_scheduler: 			bool = True