from dataclasses import dataclass


@dataclass(frozen=True)
class BasePolicy:

    enabled: bool = True