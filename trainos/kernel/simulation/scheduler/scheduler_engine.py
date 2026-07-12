from .scheduler_queue 	import SchedulerQueue
from .scheduler_status 	import SchedulerStatus
from kernel.simulation.events.event_engine import EventEngine


class SchedulerEngine:

    def __init__(self):
        self.queue = SchedulerQueue(events=[])
        self.event_engine = EventEngine()

    def process_next(self):
        event = self.queue.pop()
        if event is None:
            return None
        return self.event_engine.process(event)

    def start(self, scheduler):
        return scheduler.__class__(
            scheduler_id=scheduler.scheduler_id,
            status=SchedulerStatus.RUNNING,
        )
