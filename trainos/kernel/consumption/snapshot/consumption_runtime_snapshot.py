from dataclasses import dataclass

from kernel.consumption.runtime.consumption_lifecycle import (
    ConsumptionLifecycle,
)


@dataclass(frozen=True, slots=True)
class ConsumptionRuntimeSnapshot:

    lifecycle: ConsumptionLifecycle