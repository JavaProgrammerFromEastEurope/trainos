from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationPolicy:

    stop_on_failure: bool