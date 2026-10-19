from kernel.simulation.scheduler.scheduler_engine import SchedulerEngine

from kernel.simulation.events.simulation_event 	import SimulationEvent
from kernel.simulation.events.event_type 				import EventType
from kernel.simulation.events.event_status 			import EventStatus
from kernel.simulation.events.event_payload 		import EventPayload


def test_scheduler_engine():

    engine = SchedulerEngine()
    event = SimulationEvent(
        event_id="E2",
        tick=5,
        event_type=EventType.SECURITY,
        payload=EventPayload(
            key="threat",
            value="detected",
        ),
        status=EventStatus.CREATED,
    )
    engine.queue.add(event)
    result = engine.process_next()
    assert result.status == EventStatus.PROCESSED
