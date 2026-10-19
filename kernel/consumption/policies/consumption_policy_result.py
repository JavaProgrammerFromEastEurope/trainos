from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ConsumptionPolicyResult:

    allowed: bool
    reason: str | None = None