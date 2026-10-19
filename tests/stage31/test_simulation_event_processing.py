from kernel.simulation.events.simulation_event import SimulationEvent
from kernel.simulation.events.event_engine 		import EventEngine
from kernel.simulation.events.event_type 			import EventType
from kernel.simulation.events.event_status 		import EventStatus
from kernel.simulation.events.event_payload 	import EventPayload


def test_simulation_event_processing():

    engine = EventEngine()
    event = SimulationEvent(
        event_id="EVENT1",
        tick=100,
        event_type=EventType.POPULATION,
        payload=EventPayload(
            key="birth",
            value="resident",
        ),
        status=EventStatus.CREATED,
    )
    processed = engine.process(event)
    assert processed.status == EventStatus.PROCESSED
