from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeConfiguration:

    auto_reload: bool = False
    reload_interval_seconds: int = 60