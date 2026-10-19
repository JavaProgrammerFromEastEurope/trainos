from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class QueueSnapshot:

    queued_tasks: int
