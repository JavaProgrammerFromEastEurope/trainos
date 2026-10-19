from kernel.integration.contracts.integration_contract import IntegrationContract

from kernel.integration.contracts.contract_type import ContractType
from kernel.integration.events.integration_event import IntegrationEvent
from kernel.integration.events.integration_event_engine import IntegrationEventEngine
from kernel.integration.events.integration_event_type import IntegrationEventType
from kernel.integration.events.integration_event_status import IntegrationEventStatus


def test_integration_event_process():

    contract = IntegrationContract(
        contract_id="C2",
        contract_type=ContractType.SECURITY,
        name="ThreatDetected",
    )
    event = IntegrationEvent(
        event_id="EVENT2",
        event_type=IntegrationEventType.SECURITY,
        contract=contract,
        status=IntegrationEventStatus.PUBLISHED,
    )

    engine = IntegrationEventEngine()
    processed = engine.process(event)
    assert processed.status == IntegrationEventStatus.PROCESSED
