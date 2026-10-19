from kernel.integration.message_bus.message import (
    Message,
)

from kernel.integration.message_bus.message_queue import MessageQueue
from kernel.integration.message_bus.message_status import MessageStatus
from kernel.integration.contracts.integration_contract import IntegrationContract
from kernel.integration.contracts.contract_type import ContractType
from kernel.integration.events.integration_event import IntegrationEvent
from kernel.integration.events.integration_event_type import IntegrationEventType
from kernel.integration.events.integration_event_status import IntegrationEventStatus


def test_message_queue():

    contract = IntegrationContract(
        contract_id="C1",
        contract_type=ContractType.POPULATION,
        name="ResidentCreated",
    )
    event = IntegrationEvent(
        event_id="E1",
        event_type=IntegrationEventType.POPULATION,
        contract=contract,
        status=IntegrationEventStatus.CREATED,
    )
    message = Message(
        message_id="M1",
        event=event,
        status=MessageStatus.CREATED,
    )

    queue = MessageQueue(messages=[])
    queue.add(message)

    assert queue.pop().message_id == "M1"
    assert queue.pop() is None
