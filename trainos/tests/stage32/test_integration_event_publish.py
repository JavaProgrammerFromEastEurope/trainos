from kernel.integration.contracts.integration_contract import IntegrationContract

from kernel.integration.contracts.contract_type import ContractType
from kernel.integration.events.integration_event import IntegrationEvent
from kernel.integration.events.integration_event_engine import IntegrationEventEngine
from kernel.integration.events.integration_event_type import IntegrationEventType
from kernel.integration.events.integration_event_status import IntegrationEventStatus


def test_integration_event_publish():
    contract = IntegrationContract(
        contract_id="C1",
        contract_type=ContractType.POPULATION,
        name="ResidentCreated",
    )
    event = IntegrationEvent(
        event_id="EVENT1",
        event_type=IntegrationEventType.POPULATION,
        contract=contract,
        status=IntegrationEventStatus.CREATED,
    )

    engine = IntegrationEventEngine()
    published = engine.publish(event)
    assert published.status == IntegrationEventStatus.PUBLISHED
