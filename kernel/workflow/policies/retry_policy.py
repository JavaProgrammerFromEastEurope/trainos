from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetryPolicy:

    max_attempts: int
    delay_ticks: 	int