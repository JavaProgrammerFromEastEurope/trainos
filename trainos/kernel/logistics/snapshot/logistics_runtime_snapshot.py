from dataclasses import dataclass

from kernel.logistics.runtime.logistics_lifecycle import LogisticsLifecycle


@dataclass(frozen=True, slots=True)
class LogisticsRuntimeSnapshot:
  
    lifecycle: LogisticsLifecycle
