from kernel.integration.message_bus.message_bus_engine import MessageBusEngine

from kernel.integration.message_bus.message import Message
from kernel.integration.message_bus.message_status import MessageStatus
from kernel.integration.contracts.integration_contract import IntegrationContract
from kernel.integration.contracts.contract_type import ContractType
from kernel.integration.events.integration_event import IntegrationEvent
from kernel.integration.events.integration_event_type import IntegrationEventType
from kernel.integration.events.integration_event_status import IntegrationEventStatus


def test_message_bus():

    contract = IntegrationContract(
        contract_id="C1",
        contract_type=ContractType.SECURITY,
        name="ThreatDetected",
    )
    event = IntegrationEvent(
        event_id="E1",
        event_type=IntegrationEventType.SECURITY,
        contract=contract,
        status=IntegrationEventStatus.CREATED,
    )
    message = Message(
        message_id="M1",
        event=event,
        status=MessageStatus.CREATED,
    )

    engine = MessageBusEngine()
    engine.publish(message)
    delivered = engine.deliver()

    assert delivered.status == MessageStatus.DELIVERED
