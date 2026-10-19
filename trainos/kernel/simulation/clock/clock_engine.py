from .simulation_clock 	import SimulationClock
from .clock_status 			import ClockStatus


class ClockEngine:

    def start(
        self,
        clock: SimulationClock,
    ) -> SimulationClock:
        return SimulationClock(
            clock_id=clock.clock_id,
            tick=clock.tick,
            status=ClockStatus.RUNNING,
        )

    def advance(
        self,
        clock: SimulationClock,
    ) -> SimulationClock:
        return SimulationClock(
            clock_id=clock.clock_id,
            tick=clock.tick + 1,
            status=clock.status,
        )

    def pause(
        self,
        clock: SimulationClock,
    ) -> SimulationClock:
        return SimulationClock(
            clock_id=clock.clock_id,
            tick=clock.tick,
            status=ClockStatus.PAUSED,
        )
