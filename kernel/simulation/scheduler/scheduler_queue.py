from dataclasses import dataclass

from kernel.simulation.events.simulation_event import SimulationEvent


@dataclass(slots=True)
class SchedulerQueue:

    events: list[SimulationEvent]

    def add(
        self,
        event: SimulationEvent,
    ) -> None:
        self.events.append(event)

    def pop(self) -> SimulationEvent | None:
        if not self.events:
            return None
        return self.events.pop(0)
