from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuditStatistics:

    executed_steps: int
    failed_steps: 	int