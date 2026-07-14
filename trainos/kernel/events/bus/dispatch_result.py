from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DispatchResult:

    delivered: int