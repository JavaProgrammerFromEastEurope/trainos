from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExecutionStatistics:

    duration_ms: int