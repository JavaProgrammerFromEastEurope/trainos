from kernel.simulation.scheduler.scheduler_queue import SchedulerQueue
from kernel.simulation.events.simulation_event import SimulationEvent
from kernel.simulation.events.event_type 			import EventType
from kernel.simulation.events.event_status 		import EventStatus
from kernel.simulation.events.event_payload 	import EventPayload


def test_scheduler_queue():

    queue = SchedulerQueue(events=[])
    event = SimulationEvent(
        event_id="E1",
        tick=1,
        event_type=EventType.GOVERNANCE,
        payload=EventPayload(
            key="decision",
            value="approved",
        ),
        status=EventStatus.CREATED,
    )
    queue.add(event)
    result = queue.pop()

    assert result.event_id == "E1"
    assert queue.pop() is None
