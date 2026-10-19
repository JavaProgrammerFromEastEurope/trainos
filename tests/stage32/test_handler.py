from kernel.integration.handlers.handler_engine import HandlerEngine

from kernel.integration.contracts.integration_contract import IntegrationContract
from kernel.integration.contracts.contract_type import ContractType
from kernel.integration.events.integration_event import IntegrationEvent
from kernel.integration.events.integration_event_status import IntegrationEventStatus
from kernel.integration.events.integration_event_type import IntegrationEventType


def test_handler():

    contract = IntegrationContract(
        contract_id="C1",
        contract_type=ContractType.HEALTHCARE,
        name="DiseaseDetected",
    )
    event = IntegrationEvent(
        event_id="E1",
        event_type=IntegrationEventType.HEALTHCARE,
        contract=contract,
        status=IntegrationEventStatus.PROCESSED,
    )

    result = HandlerEngine().handle(event)
    assert result.success is True
