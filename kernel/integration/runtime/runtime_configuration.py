from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IntegrationRuntimeConfiguration:

    auto_process: bool = True
    max_messages_per_cycle: int = 100